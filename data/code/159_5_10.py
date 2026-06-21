def extract_odd_numbers(data):
    return tuple(num for num in data if num % 2 != 0)

if __name__ == '__main__':
    sample_sequence = (15, 22, 37, 44, 59, 68)
    odd_numbers = extract_odd_numbers(sample_sequence)
    print(odd_numbers)