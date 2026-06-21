ODD_THRESHOLD = 2

def extract_odds(sequence):
    return tuple(num for num in sequence if num % ODD_THRESHOLD != 0)

if __name__ == '__main__':
    sample_sequence = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    odd_numbers = extract_odds(sample_sequence)
    print(odd_numbers)