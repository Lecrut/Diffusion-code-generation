def compare_lengths(len_a, len_b):
    if len_a > len_b:
        return 1
    elif len_a < len_b:
        return -1
    else:
        return 0

def length_comparison_generator(lengths_a, lengths_b):
    for a, b in zip(lengths_a, lengths_b):
        yield compare_lengths(a, b)

if __name__ == '__main__':
    sequence_a = [10, 5, 10, 20]
    sequence_b = [10, 8, 10, 15]
    
    results = list(length_comparison_generator(sequence_a, sequence_b))
    
    print(results)