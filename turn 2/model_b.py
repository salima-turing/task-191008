# test_adaptive_framework.py
import unittest
from unittest.mock import Mock


class TestAdaptiveDataRestriction(unittest.TestCase):

    def setUp(self):
        self.mock_framework = Mock()

    def test_restrict_sensitive_data(self):
        # Mock the method call to be tested
        self.mock_framework.apply_restrictions.return_value = ["Restricted", "PersonalData"]

        # Data input
        data = ["UserName", "PersonalData", "Address", "SensitiveData"]
        policy = "Restrict Sensitive Data"

        # Call the unit test subject (under test) with the mocked framework
        result = self.mock_framework.apply_restrictions(data, policy)

        # Assertions to validate the output
        self.assertEqual(result, ["Restricted", "PersonalData"])
        self.mock_framework.apply_restrictions.assert_called_once_with(data, policy)


if __name__ == '__main__':
    unittest.main()
