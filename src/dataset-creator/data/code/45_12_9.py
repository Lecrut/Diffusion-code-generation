import logging
class SummationHandler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    def validate_input(self, value1, value2):
        if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
            raise TypeError("Both inputs must be integers or floats.")
        return True
    def calculate_sum(self, value1, value2):
        try:
            self.validate_input(value1, value2)
            result = value1 + value2
            self.logger.info(f"Sum calculated successfully for {value1} and {value2}: {result}")
            return result
        except Exception as e:
            error_msg = f"Error during summation of {value1} and {value2}: {str(e)}"
            self.logger.error(error_msg)
            raise
if __name__ == '__main__':
    handler = SummationHandler()
    sample_values_1 = 42.5
    sample_values_2 = -98
    try:
        final_result = handler.calculate_sum(sample_values_1, sample_values_2)
        print(f"Final Result: {final_result}")
    except Exception as e:
        print("An error occurred.")