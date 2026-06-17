import logging
class ValueSummator:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    def add(self, a, b):
        try:
            val_a = float(a) if isinstance(a, str) else a
            val_b = float(b) if isinstance(b, str) else b
            result = val_a + val_b
            self.logger.info(f"Summing {val_a} and {val_b}: Result is {result}")
            return result
        except ValueError as e:
            error_msg = f"Invalid input type or value. Error details: {str(e)}"
            self.logger.error(error_msg)
            raise
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    summator = ValueSummator()
    sample_a = 10.5
    sample_b = "20"
    try:
        total = summator.add(sample_a, sample_b)
        print(f"The final sum is {total}")
    except Exception as e:
        print("An error occurred during calculation.")