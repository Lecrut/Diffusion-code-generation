from typing import Literal
def calculate_distance(value: float) -> int:
    return round(abs(value))
if __name__ == '__main__':
    distances = [calculate_distance(1234567890), calculate_distance(-987654321)]