def length_difference(len_a: int, len_b: int) -> int:
    """Return the absolute difference between two lengths using conditional expressions."""
    return (len_a - len_b) if len_a >= len_b else -(len_a - len_b)

if __name__ == '__main__':
    result = length_difference(10, 4)
    print(result)