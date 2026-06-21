def decimal_to_binary_list(numbers):
    return [bin(n)[2:] for n in numbers]

if __name__ == '__main__':
    sample_numbers = [0, 1, 2, 5, 10, 255, 1024]
    result = decimal_to_binary_list(sample_numbers)
    print(result)