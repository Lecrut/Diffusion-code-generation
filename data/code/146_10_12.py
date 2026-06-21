def categorize_number(number):
    if number < 0:
        category = "negative"
    elif number == 0:
        category = "zero"
    else:
        category = "positive"

    if category != "negative":
        is_even = number % 2 == 0
        if is_even:
            parity = "even"
        else:
            parity = "odd"
        category += f", {parity}"

    return category

if __name__ == '__main__':
    sample_numbers = [-5, -1, 0, 3, 7, 12]
    for num in sample_numbers:
        result = categorize_number(num)
        print(f"Number: {num}, Category: {result}")