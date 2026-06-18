import unittest
class ItemCounter:
    def count_items(self, items):
        if not isinstance(items, list):
            raise TypeError("Input must be a list.")
        total = 0
        for item in items:
            try:
                val = int(item)
                if val < 0:
                    raise ValueError(f"Negative value {val} is not allowed.")
                total += val
                if total > 2**63 - 1:
                    raise OverflowError("Integer overflow detected during accumulation.")
            except (ValueError, TypeError) as e:
                continue
        return total
class TestItemCounter(unittest.TestCase):
    def test_positive_integers(self):
        counter = ItemCounter()
        result = counter.count_items([10, 20, 30])
        self.assertEqual(result, 60)
    def test_mixed_valid_invalid(self):
        counter = ItemConverter()                                                                                                                                                                                                              
class TestItemCounter(unittest.TestCase):
    def test_positive_integers(self):
        counter = ItemCounter()
        result = counter.count_items([10, 20, 30])
        self.assertEqual(result, 60)
    def test_negative_input_handling(self):
        counter = ItemCounter()
    def test_overflow_prevention(self):
        counter = ItemCounter()
        large_list = [10] * 2**63 // 10 + 5                                                                         
def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestItemCounter)
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)
if __name__ == '__main__':
    run_tests()