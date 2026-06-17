import logging
class ValueSummator:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    def validate_input(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both inputs must be numeric.")
        return True
    def sum_values(self, a, b):
        try:
            self.validate_input(a, b)
            result = a + b
            if result > 10**9 or result < -10**9:
                raise OverflowError("Result exceeds safe integer range.")
            return result
        except Exception as e:
            error_msg = f"Summation failed for inputs {a} and {b}: {str(e)}"
            self.logger.error(error_msg)
            raise
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    summator = ValueSummator()
    sample_a = 42.5
    sample_b = 10
    try:
        total = summator.sum_values(sample_a, sample_b)
        print(f"Calculated sum: {total}")
    except Exception as e:
        print(f"Error occurred: {e}")