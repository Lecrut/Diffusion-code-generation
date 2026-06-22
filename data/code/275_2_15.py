def product_of_tuple(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

if __name__ == '__main__':
    sample_numbers = (2, 3, 4)
    print(product_of_tuple(sample_numbers))