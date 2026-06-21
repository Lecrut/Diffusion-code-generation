def sort_two_floats(a: float, b: float) -> list[float]:
    if a <= b:
        return [a, b]
    return [b, a]

if __name__ == '__main__':
    result = sort_two_floats(3.14, 1.59)
    print(result)