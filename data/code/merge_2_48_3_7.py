import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class DivisionCalculator:
    def divide(self, dividend, divisor):
        try:
            if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
                raise TypeError("Both operands must be numeric.")
            result = dividend / divisor
            logger.info(f"Division successful: {dividend} / {divisor} = {result}")
            return result
        except ZeroDivisionError as e:
            logger.error(f"Zero division error occurred for inputs ({dividend}, {divisor}): {e}")
            raise
        except TypeError as e:
            logger.error(f"Type error during calculation: {e}")
            raise
if __name__ == '__main__':
    calc = DivisionCalculator()
    test_cases = [
        (10, 2),
        (5.5, 1.1),
        (7, 0),
        ("abc", 3),
        (-4, -8)
    ]
    for val_dividend in range(len(test_cases)):
        dividend = test_cases[val_dividend][0]
        divisor = test_cases[val_dividend][1]
        try:
            result = calc.divide(dividend, divisor)
            print(f"Result of {dividend} / {divisor}: {result}")
        except Exception as ex:
            logger.critical(f"Exception raised for inputs ({dividend}, {divisor}): {ex}")