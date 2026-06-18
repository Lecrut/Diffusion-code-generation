import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class DivisionCalculator:
    def divide(self, dividend: float, divisor: float) -> float:
        if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
            raise TypeError("Both operands must be numeric.")
        if divisor == 0.0:
            logger.error(f"Division by zero error with dividend {dividend} and divisor {divisor}")
            raise ZeroDivisionError(f"Cannot divide by zero: {divisor}")
        result = dividend / divisor
        logger.info(f"Calculated division of {dividend} divided by {divisor}: {result}")
        return result
if __name__ == '__main__':
    calc = DivisionCalculator()
    try:
        res1 = calc.divide(20, 4)
        print(f"Result of normal division: {res1}")
    except Exception as e:
        logger.error(f"Unexpected error in test case 1: {e}")
    try:
        res2 = calc.divide(50, 0)
        print(f"Result of division by zero (should not happen): {res2}")
    except ZeroDivisionError as e:
        logger.warning("Caught expected ZeroDivisionError")
    try:
        res3 = calc.divide(10, "5")
        print(f"Result of non-numeric division (should not happen): {res3}")
    except TypeError as e:
        logger.warning("Caught expected TypeError for invalid type")
    try:
        res4 = calc.divide(-10, -2)
        print(f"Result of negative division: {res4}")
    except Exception as e:
        logger.error(f"Unexpected error in test case 4: {e}")
    try:
        res5 = calc.divide(1, 3)
        print(f"Result of float division (repeating decimal): {res5:.6f}")
    except Exception as e:
        logger.error(f"Unexpected error in test case 5: {e}")