def categorize_number(num):
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

    return f"{num} is {category} and {parity}"

if __name__ == '__main__':
    sample_values = [-5, 0, 3, 10]
    for value in sample_values:
        print(categorize_number(value))