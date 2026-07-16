# test_agentvaultx.py
"""
Tests for AgentVaultX module.
"""

import unittest
from agentvaultx import AgentVaultX

class TestAgentVaultX(unittest.TestCase):
    """Test cases for AgentVaultX class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AgentVaultX()
        self.assertIsInstance(instance, AgentVaultX)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AgentVaultX()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
