def generate_even_numbers(start, count):
    if start % 2 != 0:
        raise ValueError("Start value must be even")
    if count < 0:
        raise ValueError("Count must be non-negative")
    
    return [start + i * 2 for i in range(count)]

if __name__ == '__main__':
    sample_start = 2
    sample_count = 10
    result = generate_even_numbers(sample_start, sample_count)
    print(result)