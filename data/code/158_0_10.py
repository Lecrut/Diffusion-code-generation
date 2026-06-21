def generate_even_numbers(max_value):
    if not isinstance(max_value, int) or max_value < 1:
        raise ValueError("max_value must be a positive integer")
    
    return [x for x in range(1, max_value + 1) if x % 2 == 0]

if __name__ == '__main__':
    try:
        even_numbers = generate_even_numbers(50)
        print(even_numbers)
    except ValueError as e:
        print(f"Error: {e}")