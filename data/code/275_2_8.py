def multiply_elements(numbers):
    product = 1
    for number in numbers:
        if number == 0:
            return 0
        product *= number
    return product

if __name__ == '__main__':
    sample_values = (2, 3, 4)
    print(multiply_elements(sample_values))