import sys
def sanitize_input(value: str) -> float | None:
    try:
        return float(value.strip()) if value else 0.0
    except ValueError:
        print(f"Error: Invalid numeric input '{value}'")
        return None
class Logger:
    def __init__(self, log_file=None):
        self.log_file = open(log_file or "calculator_log.txt", "a")
    def info(self, message: str) -> None:
        timestamp = f"[{sys.argv[0]}] {message}" if sys.argv else f"INFO: {message}"
        print(timestamp)
        self.log_file.write(f"{timestamp}\n")
        self.log_file.flush()
    def error(self, message: str) -> None:
        timestamp = f"[ERROR] {message}"
        print(timestamp)
        self.log_file.write(f"{timestamp}\n")
        self.log_file.flush()
def calculate_sum(a: float | int, b: float | int) -> tuple[float, bool]:
    try:
        result = a + b
        return result, True
    except Exception as e:
        print(f"Calculation failed due to error: {e}")
        Logger().error(str(e))
        return 0.0, False
if __name__ == '__main__':
    logger = Logger()
    sample_a_str = "123456789.12345"
    sample_b_str = "-987654321.98765"
    a_val = sanitize_input(sample_a_str) or 0.0
    b_val = sanitize_input(sample_b_str) or 0.0
    logger.info(f"Processing inputs: {a_val} and {b_val}")
    final_result, success = calculate_sum(a_val, b_val)
    if not success:
        sys.exit(1)
    print(f"Sum of {sample_a_str} + {sample_b_str} = {final_result:.5f}")