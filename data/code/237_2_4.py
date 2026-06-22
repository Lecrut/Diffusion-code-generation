def generate_powers_of_two(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    powers = [1 << i for i in range(n)]
    return powers

if __name__ == '__main__':
    try:
        sample_values = generate_powers_of_two(10)
        print(sample_values)
    except ValueError as e:
        print(e)