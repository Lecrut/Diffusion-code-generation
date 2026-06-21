def categorize_number(num):
    if num < 0:
        category = 'negative'
    elif num == 0:
        category = 'zero'
    else:
        category = 'positive'
    
    if num % 2 == 0:
        parity = 'even'
    else:
        parity = 'odd'
    
    return f"{category}, {parity}"

if __name__ == '__main__':
    sample_numbers = [-5, 0, 3, 10]
    for number in sample_numbers:
        result = categorize_number(number)
        print(f"Number: {number}, Category: {result}")