def decimal_to_binary(numbers):
    return [format(n, 'b') for n in numbers]

if __name__ == '__main__':
    sample_numbers = [0, 1, 5, 10, 255]
    result = decimal_to_binary(sample_numbers)
    print(result)