a = 10
b = 5

def calculate_difference(x: int, y: int) -> int:
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Both inputs must be integers.")
    return x - y

if __name__ == '__main__':
    result = calculate_difference(a, b)
    print(result)