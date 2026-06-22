def compare_lengths(length1, length2):
    if length1 < length2:
        return "less than"
    if length1 > length2:
        return "greater than"
    return "equal to"

def compare_lengths_generator(sequence_a, sequence_b):
    for item_a, item_b in zip(sequence_a, sequence_b):
        result = compare_lengths(item_a, item_b)
        yield result

if __name__ == '__main__':
    lengths_a = [10, 20, 30, 40, 50]
    lengths_b = [15, 20, 25, 40, 60]
    results = list(compare_lengths_generator(lengths_a, lengths_b))
    for res in results:
        print(res)