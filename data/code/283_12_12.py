def locate_first_repetition(sequence):
    encountered = set()
    for element in sequence:
        if element in encountered:
            return element
        encountered.add(element)
    return None

if __name__ == '__main__':
    sample_sequence = [4, 5, 6, 7, 8, 9, 10, 2, 3, 1]
    print(locate_first_repetition(sample_sequence))