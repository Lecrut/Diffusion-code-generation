def decimal_to_binary_strings(numbers):
    return [bin(n)[2:] if n >= 0 else '-' + bin(n)[3:] for n in numbers]

if __name__ == '__main__':
    sample_numbers = [0, 5, 10, 255, -10]
    result = decimal_to_binary_strings(sample_numbers)
    print(result)