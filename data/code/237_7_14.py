def generate_even_numbers(start, count):
    if not isinstance(start, int) or start < 2:
        raise ValueError("Start value must be an integer greater than or equal to 2")
    if not isinstance(count, int) or count <= 0:
        raise ValueError("Count must be a positive integer")

    return list(range(start, start + count * 2, 2))

if __name__ == '__main__':
    start = 2
    count = 10
    result = generate_even_numbers(start, count)
    print(result)