def sequential_sum_generator(iterable1, iterable2):
    it1 = iter(iterable1)
    it2 = iter(iterable2)
    while True:
        try:
            val1 = next(it1)
            val2 = next(it2)
            yield val1 + val2
        except StopIteration:
            return
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [5, 6, 7, 8]
    print("Sequential sums:")
    for s in sequential_sum_generator(list_a, list_b):
        print(s)