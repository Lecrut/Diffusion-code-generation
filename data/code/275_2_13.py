def product_tuple(numbers):
    result = 1
    for number in numbers:
        if number == 0:
            return 0
        result *= number
    return result

if __name__ == '__main__':
    sample_values = (2, 3, 4)
    print(product_tuple(sample_values))