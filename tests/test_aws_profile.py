import os
import unittest
import boto3
from unittest.mock import patch
from providers.aws.ec2 import AwsEc2

class TestAwsProfile(unittest.TestCase):
    @patch.dict(os.environ, {"AWS_PROFILE": "test_profile"})
    def test_aws_profile_support(self):
        # Mocking boto3.client to avoid actual AWS calls
        with patch('boto3.client') as mock_client:
            # Create an instance of AwsEc2
            aws_ec2 = AwsEc2(aws_end_point=None, aws_region='us-west-2')

            # Check if boto3.client was called with the correct arguments
            mock_client.assert_called_with(
                'ec2',
                endpoint_url=None,
                region_name='us-west-2'
            )

            # Verify that the AWS_PROFILE environment variable is set
            self.assertEqual(os.environ.get('AWS_PROFILE'), 'test_profile')

if __name__ == '__main__':
    unittest.main()
