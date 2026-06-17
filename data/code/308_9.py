def calculate_total_length(sequence):
    return sum(len(item) for item in sequence)
if __name__ == '__main__':
    sample_sequence = ["apple", "banana", "kiwi", "orange"]
    total_length = calculate_total_length(sample_sequence)
    print(total_length)