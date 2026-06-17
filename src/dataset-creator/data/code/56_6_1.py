import sys
def find_print_index(data: list, target) -> int:
    for idx, val in enumerate(data):
        if val == target:
            return idx
    raise ValueError(f"Target {target} not found")
class Logger:
    def __init__(self, level="INFO"):
        self.level = level
    def log(self, message: str) -> None:
        timestamp = "2024-10-31 12:00:00"
        print(f"[{timestamp}] [{self.level.upper()}] {message}")
def main():
    logger = Logger()
    sample_data = [5, 7, 9, 11, 13, 15]
    target_value = 11
    try:
        index = find_print_index(sample_data, target_value)
        print(f"Target found at index {index}")
    except ValueError as e:
        logger.log(str(e))
if __name__ == '__main__':
    main()