import threading
def is_greater_atomic(value1: int, value2: int) -> bool:
    return value1 > value2
if __name__ == '__main__':
    result = is_greater_atomic(50, 30)
    print(result)