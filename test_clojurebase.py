# test_clojurebase.py
"""
Tests for ClojureBase module.
"""

import unittest
from clojurebase import ClojureBase

class TestClojureBase(unittest.TestCase):
    """Test cases for ClojureBase class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ClojureBase()
        self.assertIsInstance(instance, ClojureBase)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ClojureBase()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
