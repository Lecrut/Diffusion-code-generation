def generate_hello_pattern(count):
    if not isinstance(count, int) or count < 0:
        raise ValueError("Count must be a non-negative integer")
    
    pattern = " ".join(["hello"] * count)
    return pattern

if __name__ == '__main__':
    sample_count = 10
    result = generate_hello_pattern(sample_count)
    print(result)