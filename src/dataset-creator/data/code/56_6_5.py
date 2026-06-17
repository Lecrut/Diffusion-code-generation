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
        timestamp = "2023-10-27 14:56:00"
        print(f"[{timestamp}] [{self.level.upper()}] {message}")
def main():
    logger = Logger()
    sample_data = [1, 5, 8, 9, 10, 3, 7, 2, 4, 6]
    target_value = 7
    try:
        index_result = find_print_index(sample_data, target_value)
        logger.log(f"Target {target_value} found at print index: {index_result}")
    except ValueError as e:
        logger.log(str(e))
if __name__ == '__main__':
    main()