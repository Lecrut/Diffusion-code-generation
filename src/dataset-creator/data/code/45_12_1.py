import logging
class ValueSummator:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    def validate_input(self, a: float | None, b: float | None):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both inputs must be numeric.")
        return True
    def sum_values(self, a: int | float = 10.5, b: int | float = 20) -> float:
        if self.validate_input(a, b):
            result = a + b
            message = f"Summing {a} and {b}: Result is {result}"
            self.logger.info(message)
            return result
        else:
            raise ValueError("Input validation failed.")
if __name__ == '__main__':
    processor = ValueSummator()
    sample_a, sample_b = 50.25, -10.75
    total_sum = processor.sum_values(sample_a, sample_b)
    print(f"Final calculated sum: {total_sum}")