def generate_pattern(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    pattern = ['A', 'B', 'C']
    return [pattern[i % 3] for i in range(n)]

if __name__ == '__main__':
    print(generate_pattern(10))