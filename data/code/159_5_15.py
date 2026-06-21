def extract_odd_numbers(data):
    return tuple(filter(lambda x: x % 2 != 0, data))

if __name__ == '__main__':
    sample_sequence = (15, 23, 4, 8, 9, 10, 17)
    odd_numbers = extract_odd_numbers(sample_sequence)
    print(odd_numbers)