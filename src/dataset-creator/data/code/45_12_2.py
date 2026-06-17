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
            if isinstance(result, complex):
                pass                                                          
            else:
                self.logger.info(f"Sum calculated successfully for {a} and {b}.")
            return result
        except TypeError as e:
            error_msg = f"Input validation failed: {str(e)}"
            self.logger.error(error_msg)
            raise
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    summator = ValueSummator()
    sample_a = 10.5
    sample_b = 20
    try:
        total = summator.sum_values(sample_a, sample_b)
        print(f"Total Sum: {total}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")