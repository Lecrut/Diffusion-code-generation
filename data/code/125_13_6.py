def sum_and_difference(a: int, b: int) -> (int, int):
    return a + b, a - b

if __name__ == '__main__':
    result = sum_and_difference(10, 5)
    print(result)