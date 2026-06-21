def categorize_number(num):
    if not isinstance(num, int):
        raise ValueError("Input must be an integer.")
    
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
    
    return (category, parity)

if __name__ == '__main__':
    sample_numbers = [10, -5, 0, 3, 8, -7]
    for number in sample_numbers:
        try:
            result = categorize_number(number)
            print(f"Number: {number}, Category: {result[0]}, Parity: {result[1]}")
        except ValueError as e:
            print(e)