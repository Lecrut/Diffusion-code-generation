def find_min_max(values):
    try:
        min_val = max_val = next(values)
    except StopIteration:
        raise ValueError("The generator is empty") from None

    for value in values:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value

    return {"min": min_val, "max": max_val}

if __name__ == '__main__':
    gen1 = (x**2 for x in range(5))
    gen2 = (x * 3 for x in range(-2, 4))

    result1 = find_min_max(gen1)
    print(f"Generator 1: {list(range(5))}")
    print(f"Result 1: {result1}")

    result2 = find_min_max(gen2)
    print(f"Generator 2: {list(range(-2, 4))}")
    print(f"Result 2: {result2}")