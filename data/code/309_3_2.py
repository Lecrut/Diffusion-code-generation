def sum_iterable(iterable):
    return sum(x for x in iterable)
if __name__ == '__main__':
    sample1 = (1, 2, 3, 4, 5)
    result1 = sum_iterable(sample1)
    print(f"Sum of {sample1}: {result1}")
    sample2 = [10, 20, 30]
    result2 = sum_iterable(sample2)
    print(f"Sum of {sample2}: {result2}")
    sample3 = (1.5, 2.5, 3.0)
    result3 = sum_iterable(sample3)
    print(f"Sum of {sample3}: {result3}")
    sample4 = []
    result4 = sum_iterable(sample4)
    print(f"Sum of {sample4}: {result4}")