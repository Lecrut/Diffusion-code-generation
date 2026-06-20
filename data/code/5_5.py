def compare_lengths_generator(length_a, length_b):
    if length_a < length_b:
        yield -1
    elif length_a > length_b:
        yield 1
    else:
        yield 0

def compare_multiple_pairs(pairs):
    for a, b in pairs:
        result = next(compare_lengths_generator(a, b))
        yield result

if __name__ == '__main__':
    sample_pairs = [
        (10, 5),
        (3, 3),
        (7, 12),
        (100, 50),
        (0, 1)
    ]
    results = list(compare_multiple_pairs(sample_pairs))
    print(results)