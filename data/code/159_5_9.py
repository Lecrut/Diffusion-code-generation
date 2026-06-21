def extract_odd_numbers(data):
    return tuple(filter(lambda x: x % 2 != 0, data))

if __name__ == '__main__':
    sample_sequence = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    odd_numbers = extract_odd_numbers(sample_sequence)
    print(odd_numbers)