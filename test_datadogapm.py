# test_datadogapm.py
"""
Tests for DatadogAPM module.
"""

import unittest
from datadogapm import DatadogAPM

class TestDatadogAPM(unittest.TestCase):
    """Test cases for DatadogAPM class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DatadogAPM()
        self.assertIsInstance(instance, DatadogAPM)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DatadogAPM()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
