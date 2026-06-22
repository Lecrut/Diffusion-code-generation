def convert_to_binary(numbers):
    return [bin(n)[2:] for n in numbers]

if __name__ == '__main__':
    sample_numbers = [0, 1, 10, 15, 255]
    result = convert_to_binary(sample_numbers)
    print(result)