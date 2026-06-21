def categorize_number(num):
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")
    
    if num < 0:
        category = "negative"
    elif num == 0:
        category = "zero"
    else:
        category = "positive"
    
    if num % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    
    return f"{category}, {parity}"

if __name__ == '__main__':
    sample_numbers = [-1, 0, 1, 2, -3, 4]
    for number in sample_numbers:
        result = categorize_number(number)
        print(f"Number: {number}, Category: {result}")