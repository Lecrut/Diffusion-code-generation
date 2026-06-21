def decimal_to_binary_list(numbers):
    return [bin(number)[2:] for number in numbers]

if __name__ == '__main__':
    sample_numbers = [0, 1, 2, 5, 10, 15, 255, 1024]
    result = decimal_to_binary_list(sample_numbers)
    print(result)