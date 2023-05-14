import random
from datetime import datetime, timedelta
import pandas as pd


def generate_dataset(product_mix_tools):
    start_date = "2022-01-01"
    end_date = "2023-04-30"
    data_list = []

    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    monthly_customer_number = 3000000
    seat_number = 60000
    while current_date <= datetime.strptime(end_date, "%Y-%m-%d"):
        date = current_date.strftime("%Y-%m-%d")
        if random.random() < 0.4:
            tool = "MS365 Business Basic"
        else:
            tool = random.choice(product_mix_tools)
        plan_total = random.randint(3000, 3500)
        fact_total = plan_total + random.randint(-50, 125)

        monthly_customer_number = monthly_customer_number + random.randint(-20000, 25000)
        seat_number = seat_number + random.randint(-80, 20)

        data_list.append([date, tool, fact_total, plan_total, monthly_customer_number, seat_number])
        current_date += timedelta(days=1)

    columns = ["Date", "Tool", "Fact Total", "Plan Total", "Monthly MT customer number", "Seat Number"]
    df = pd.DataFrame(data_list, columns=columns)

    return df

tools = [
    "MS Azure Active Directory Premier",
    "MS365 Exchange",
    "Salesforce Essentials",
    "Zoho One",
    "Okta",
    "OneLogin",
    "Zimbra",
    "Trello",
    "Asana",
    "Slack",
    "Microsoft Teams",
    "Zoom",
    "Jira",
    "Confluence",
    "Adobe Creative Cloud"
]

dataset = generate_dataset(tools)
print(dataset)

dataset.to_csv("customTelekomDataset.csv", index=False)
