import unittest
from app import say_Hello


class TestApp(unittest.TestCase):
    def test_say_Hello(self):
        self.assertEqual(say_Hello("AWS"), "Hello, AWS")
if __name__ == "__main__":
    unittest.main()