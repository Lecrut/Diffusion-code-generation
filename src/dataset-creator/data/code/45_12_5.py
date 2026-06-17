import logging
from typing import Union
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class SummationHandler:
    def __init__(self):
        pass
    def validate_input(self, a: float, b: float) -> bool:
        return isinstance(a, (int, float)) and isinstance(b, (int, float))
    def calculate_sum(self, a: Union[int, float], b: Union[int, float]) -> None:
        if not self.validate_input(a, b):
            logger.error(f"Invalid input types. Expected numeric values for {a} and {b}.")
            raise ValueError("Input validation failed.")
        result = a + b
        logger.info(f"Summing {a} and {b}, resulting in {result}")
if __name__ == '__main__':
    handler = SummationHandler()
    value_a: float = 10.5
    value_b: float = 20
    try:
        handler.calculate_sum(value_a, value_b)
    except ValueError as e:
        logger.error(f"Execution halted due to error: {e}")