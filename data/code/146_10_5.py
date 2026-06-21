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
    print(categorize_number(-5))
    print(categorize_number(0))
    print(categorize_number(10))