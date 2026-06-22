def triangular_numbers(count):
    if count < 1 or not isinstance(count, int):
        raise ValueError("Count must be a positive integer")
    
    return [n * (n + 1) // 2 for n in range(1, count + 1)]

if __name__ == '__main__':
    sample_count = 12
    try:
        triangular_result = triangular_numbers(sample_count)
        print(triangular_result)
    except ValueError as e:
        print(e)