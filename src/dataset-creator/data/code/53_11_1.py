def count_elements(sequence):
    return sum(1 for _ in sequence)
if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40]
    result = count_elements(sample_sequence)
    print(result)