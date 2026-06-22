def decimal_to_binary_list(numbers):
    return [bin(num)[2:] for num in numbers]

if __name__ == '__main__':
    sample_integers = [0, 1, 2, 5, 10, 15, 255, 1024]
    binary_strings = decimal_to_binary_list(sample_integers)
    print(binary_strings)