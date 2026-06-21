def get_third_element(seq):
    iterator = iter(seq)
    try:
        next(iterator)
        next(iterator)
        third = next(iterator)
        return third
    except StopIteration:
        raise IndexError("Sequence has fewer than three elements")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_third_element(sample_list)
    print(result)