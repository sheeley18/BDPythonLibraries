import requests
import base64
import json

#Variables To Input
api_token= ""
#Application To Get Projects For
application = ""
#Project To Get Issues For
project = ""

#Do Not Touch
portfoliourl = "https://poc.polaris.synopsys.com/api/portfolio/portfolios"
applicationurl = "https://poc.polaris.synopsys.com/api/portfolio/portfolios/{portfolioid}/portfolio-items"





headers = {
"accept": "application/vnd.synopsys.pm.portfolio-1+json",
"Api-Token": api_token
}
portfolioresponse = requests.get(portfoliourl, headers=headers)
if portfolioresponse.status_code == 200:
	portfolioid = portfolioresponse.json()['_items'][0]['id']
	headers = {
	"accept": "application/vnd.synopsys.pm.portfolio-items-1+json",
	"Content-Type": "application/vnd.synopsys.pm.portfolio-items-1+json",
	"Api-Token": api_token
	}
	applicationresponse = requests.get(f"https://poc.polaris.synopsys.com/api/portfolio/portfolios/{portfolioid}/portfolio-items?name={application}&_limit=10", headers=headers)
	if applicationresponse.status_code == 200:
		applicationid = applicationresponse.json()['_items'][0]['id']
		headers = {
		"accept": "application/vnd.synopsys.pm.portfolio-subitems-1+json",
		"Content-Type": "application/vnd.synopsys.pm.portfolio-subitems-1+json",
		"Api-Token": api_token
		}
		projectresponse = requests.get(f"https://poc.polaris.synopsys.com/api/portfolio/portfolio-items/{applicationid}/portfolio-sub-items?name={project}", headers=headers)
		if projectresponse.status_code == 200:
			projectid = projectresponse.json()['_items'][0]['id']
			headers = {
			"accept": "application/vnd.synopsys.polaris-one.issue-management.license-paginated-list-1+json",
			"Api-Token": api_token
			}
			issuesresponse = requests.get(f"https://poc.polaris.synopsys.com/api/specialization-layer-service/licenses/_actions/list?portfolioSubItemId={projectid}&_includeAttributes=true", headers=headers)
			if issuesresponse.status_code == 200:
				items = issuesresponse.json()
				name_items = []
				for item in items['_items']:
					name_items.append(item['name'])
				for name in name_items:
					print(name)

			else:
				print(f"Request failed with status code: {issuesresponse.status_code}")
