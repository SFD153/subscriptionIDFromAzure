from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.subscription import SubscriptionClient

# Replace the placeholders with your own values
username = ''
password = ''
tenant_id = "b8cb644c-f583-4be4-8c0d-9b9313735f23"
client_id = "1cfead55-88e7-4722-b618-e02b377d4b09"
client_secret = "wko8Q~rdyRZ4YJOnFhOvG12rMUEMX7~ovikAqa.D"

# Create the credentials object
credentials = ServicePrincipalCredentials(
    client_id=client_id,
    secret=client_secret,
    tenant=tenant_id,
    username=username,
    password=password
)

# Create the subscription client
subscription_client = SubscriptionClient(credentials)

# Get the list of subscriptions
subscription_list = subscription_client.subscriptions.list()

# Print the subscription IDs
for subscription in subscription_list:
    print(subscription.subscription_id)