def categorize_number(num):
    if num < 0:
        category = "negative"
    elif num == 0:
        category = "zero"
    else:
        category = "positive"

    if num % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"

    return category, even_odd

if __name__ == '__main__':
    sample_numbers = [10, -5, 0, 3, -8]
    for number in sample_numbers:
        result = categorize_number(number)
        print(f"Number: {number}, Category: {result[0]}, Even/Odd: {result[1]}")