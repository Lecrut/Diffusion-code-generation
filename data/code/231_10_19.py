def generate_pattern(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    pattern = ['A', 'B', 'C']
    result = []
    for i in range(n):
        result.append(pattern[i % 3])
    return result

if __name__ == '__main__':
    sample_output = generate_pattern(15)
    print(sample_output)