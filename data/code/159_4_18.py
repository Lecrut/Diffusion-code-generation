def extract_odd_values(numbers):
    odd_values = []
    for number in numbers:
        if number & 1:
            odd_values.append(number)
    return odd_values

if __name__ == '__main__':
    sample_values = [2, 4, 6, 8, 10, 11, 13, 15]
    result = extract_odd_values(sample_values)
    print(result)