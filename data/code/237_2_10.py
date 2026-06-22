def generate_powers_of_two(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")
    
    powers = []
    for i in range(n):
        power = 2 << i
        powers.append(power)
    
    return powers

if __name__ == '__main__':
    sample_value = 10
    result = generate_powers_of_two(sample_value)
    print(result)