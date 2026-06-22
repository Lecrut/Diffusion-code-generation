def compare_lengths_generator(lengths_a, lengths_b):
    for a, b in zip(lengths_a, lengths_b):
        if a > b:
            yield 1
        elif a < b:
            yield -1
        else:
            yield 0

if __name__ == '__main__':
    a_vals = [5, 10, 3, 8, 2]
    b_vals = [3, 10, 7, 8, 9]
    results = list(compare_lengths_generator(a_vals, b_vals))
    print(results)