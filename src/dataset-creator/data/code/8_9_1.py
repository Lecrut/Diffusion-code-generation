def sequential_sum_generator(iterable1, iterable2):
    it1 = iter(iterable1)
    it2 = iter(iterable2)
    current1 = None
    current2 = None
    while True:
        try:
            val1 = next(it1)
            current1 = val1
        except StopIteration:
            try:
                val2 = next(it2)
                current2 = val2
            except StopIteration:
                return
        if current1 is not None and current2 is not None:
            yield current1 + current2
        elif current1 is not None:
            yield current1
        elif current2 is not None:
            yield current2
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [10, 20, 30, 40]
    print("Sums of elements from two input iterables sequentially:")
    for s in sequential_sum_generator(list_a, list_b):
        print(s)