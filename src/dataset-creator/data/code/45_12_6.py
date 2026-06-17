import logging
class SummationHandler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    def add_values(self, a, b):
        try:
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError("Both inputs must be numeric.")
            result = a + b
            self.logger.info(f"Summing {a} and {b}. Result: {result}")
            return result
        except Exception as e:
            error_msg = f"Error during summation: {str(e)}"
            self.logger.error(error_msg)
            raise
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    handler = SummationHandler()
    val1 = 42.5
    val2 = 87
    try:
        total = handler.add_values(val1, val2)
        print(f"Total sum is {total}")
    except Exception as e:
        print("An error occurred.")