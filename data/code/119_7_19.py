def reverse_floats(a: float, b: float) -> (float, float):
    return b, a

if __name__ == '__main__':
    original_values = (3.14, 2.71)
    reversed_values = reverse_floats(*original_values)
    print(reversed_values)