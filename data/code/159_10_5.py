def generate_odd_numbers(limit):
    if not isinstance(limit, int) or limit < 1:
        raise ValueError("Limit must be a positive integer")
    
    odd_numbers = [num for num in range(1, limit + 1) if num % 2 != 0]
    return odd_numbers

if __name__ == '__main__':
    sample_limit = 50
    result = generate_odd_numbers(sample_limit)
    print(result)