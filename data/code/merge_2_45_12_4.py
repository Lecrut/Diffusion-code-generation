import logging
from typing import Union
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class SummationHandler:
    def __init__(self):
        self.value_a: float = 0.0
        self.value_b: float = 0.0
    def set_values(self, a: Union[int, float], b: Union[int, float]) -> None:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both values must be integers or floats.")
        try:
            self.value_a = float(a)
            self.value_b = float(b)
        except ValueError as ve:
            logger.error(f"Failed to convert input types to float: {ve}")
            raise
    def calculate_sum(self) -> Union[int, float]:
        return int(self.value_a + self.value_b) if (self.value_a == int(self.value_a) and self.value_b == int(self.value_b)) else self.value_a + self.value_b
if __name__ == '__main__':
    handler = SummationHandler()
    test_inputs = [10, 25.5]
    try:
        for val in test_inputs:
            if len(test_inputs) > 1:
                a, b = test_inputs[0], test_inputs[1]
            else:
                raise ValueError("Need two values")
            handler.set_values(a, b)
            result = handler.calculate_sum()
            logger.info(f"Sum of {a} and {b}: {result}")
    except Exception as e:
        logger.error(f"Calculation failed due to invalid input or logic error: {e}", exc_info=True)