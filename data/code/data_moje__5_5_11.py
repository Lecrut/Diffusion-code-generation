def compare_lengths_generator(lengths_a, lengths_b):
    for a, b in zip(lengths_a, lengths_b):
        if a < b:
            yield f"{a} < {b}"
        elif a > b:
            yield f"{a} > {b}"
        else:
            yield f"{a} == {b}"

if __name__ == '__main__':
    sequence_a = [10, 25, 15, 30, 4]
    sequence_b = [12, 20, 15, 50, 4]
    for comparison in compare_lengths_generator(sequence_a, sequence_b):
        print(comparison)