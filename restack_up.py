import os
from restack_sdk_cloud import RestackCloud

async def main():
    # Initialize the RestackCloud client with the SDK token from environment variables
    restack_cloud_client = RestackCloud(os.getenv('RESTACK_SDK_TOKEN'))

    # Define the frontend application configuration
    lightdash = {
        'name': 'lightdash',
        'dockerFilePath': '/dockerfile',
        'dockerBuildContext': 'lightdash',
     
    }

    # Configure the stack with the applications
    await restack_cloud_client.stack({
        'name': 'lightdash-prod environment python',
        'previewEnabled': False,
        'applications': [lightdash],
    })

    # Deploy the stack
    await restack_cloud_client.up()

# Run the main function
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())