"""
Llama module tests
"""

import unittest

from txtai.pipeline import LLM


class TestLlama(unittest.TestCase):
    """
    llama.cpp tests.
    """

    def testGeneration(self):
        """
        Test generation with llama.cpp
        """

        # Test model generation with llama.cpp
        model = LLM("TheBloke/TinyLlama-1.1B-Chat-v0.3-GGUF/tinyllama-1.1b-chat-v0.3.Q2_K.gguf")
        self.assertEqual(model("2 + 2 = ", maxlength=10, seed=0, stop=["."]), "4")
