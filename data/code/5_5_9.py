def compare_lengths_generator(lengths_a, lengths_b):
    iterator_a = iter(lengths_a)
    iterator_b = iter(lengths_b)
    while True:
        try:
            val_a = next(iterator_a)
            val_b = next(iterator_b)
        except StopIteration:
            break
        if val_a < val_b:
            yield -1
        elif val_a > val_b:
            yield 1
        else:
            yield 0

if __name__ == '__main__':
    list_a = [10, 20, 5, 30]
    list_b = [5, 25, 5, 15]
    results = list(compare_lengths_generator(list_a, list_b))
    print(results)