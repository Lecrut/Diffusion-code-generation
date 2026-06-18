import logging
class ValueSummator:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    def sum_values(self, a: float, b: float):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both inputs must be numeric.")
        result = a + b
        try:
            self.logger.info(f"Summing {a} and {b}. Result: {result}")
            return result
        except Exception as e:
            self.logger.error(f"Error during summation: {e}", exc_info=True)
            raise
if __name__ == '__main__':
    calculator = ValueSummator()
    try:
        val1 = 42.5
        val2 = 87
        total = calculator.sum_values(val1, val2)
        print(f"Total Sum: {total}")
    except Exception as e:
        print(f"Calculation failed due to error: {e}")