def convert_to_binary(numbers):
    return [bin(n)[2:] if n >= 0 else '-' + bin(n)[3:] for n in numbers]

if __name__ == '__main__':
    sample_numbers = [5, 10, 0, -1, 255]
    result = convert_to_binary(sample_numbers)
    print(result)