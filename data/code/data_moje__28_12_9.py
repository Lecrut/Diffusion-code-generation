def sort_two_floats(a: float, b: float) -> list:
    return [a, b] if a <= b else [b, a]

if __name__ == '__main__':
    result = sort_two_floats(3.14, 2.71)
    print(result)