def find_largest_number(sequence):
    largest = None
    for number in sequence:
        if largest is None or number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_sequence = [3.14, 2.71, 1.41, 9.81, 6.28]
    print(find_largest_number(sample_sequence))