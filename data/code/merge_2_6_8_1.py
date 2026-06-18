import threading
def is_greater_atomic(value1: float, value2: float) -> bool:
    return value1 > value2
if __name__ == '__main__':
    result = is_greater_atomic(5.0, 3.0)
    print(result)