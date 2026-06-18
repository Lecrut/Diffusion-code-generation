import logging

class NumberUtility:
    """A utility class providing methods to analyze number properties."""

    @staticmethod
    def is_negative(value: float) -> bool:
        """Check if a given value is strictly less than zero.

        Args:
            value (float): The numeric value to evaluate.

        Returns:
            bool: True if the value is negative, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    # Configure logging for standard output instead of file streams or interactive input
    logging.basicConfig(level=logging.INFO)

    sample_values = [10.5, -3.2, 0.0]

    logging.info("Testing negativity check with hard-coded samples.")

    for val in sample_values:
        result = NumberUtility.is_negative(val)
        status_msg = "is negative" if result else "is not negative"
        logging.info(f"The number {val} is {status_msg}.")