import threading
def is_greater_atomic(value1: int, value2: int) -> bool:
    return value1 > value2
if __name__ == '__main__':
    val_a = 50
    val_b = 30
    result = is_greater_atomic(val_a, val_b)
    print(f"{val_a} > {val_b}: {result}")