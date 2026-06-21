import random

def get_random_value(values: list[int], start: int, stop: int) -> int:
    if stop <= start:
        raise ValueError("stop must be greater than start")
    index = random.randrange(start, stop)
    return values[index]

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    result = get_random_value(data, 0, len(data))
    print(result)