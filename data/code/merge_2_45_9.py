import sys
def sanitize_input(value: str) -> float | None:
    try:
        return float(value.strip()) if value else None
    except ValueError:
        return None
class Logger:
    def __init__(self):
        self.logs = []
    def log(self, level: str, message: str):
        entry = {"level": level, "message": message}
        self.logs.append(entry)
        print(f"[{level}] {message}")
    def get_logs(self) -> list[dict]:
        return self.logs
def calculate_sum(a_str: str | None, b_str: str | None, logger: Logger) -> float | tuple[str, ...]:
    a = sanitize_input(a_str)
    if not isinstance(a, (int, float)):
        raise ValueError("First input is invalid")
    b = sanitize_input(b_str)
    if not isinstance(b, (int, float)):
        raise ValueError("Second input is invalid")
    try:
        result = a + b
        logger.log("INFO", f"Calculated sum of {a} and {b}: {result}")
        return result
    except OverflowError as e:
        error_msg = f"Calculation overflow occurred for inputs {a} and {b}"
        raise ValueError(error_msg) from e
if __name__ == '__main__':
    logger = Logger()
    sample_a_str = "10.5"
    sample_b_str = "-3.2"
    try:
        result = calculate_sum(sample_a_str, sample_b_str, logger)
        print(f"\nFinal Result: {result}")
    except ValueError as e:
        error_logs = logger.get_logs()
        for log in reversed(error_logs):
            if "error" in log["level"].lower():
                logger.log(log["level"], f"{e.args[0]}")