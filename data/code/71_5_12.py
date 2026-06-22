def get_middle(iterable):
    try:
        iterator = iter(iterable)
        first = next(iterator)
        second = next(iterator)
        last = first
        prev = second
        for current in iterator:
            prev = last
            last = current
        if prev is None:
            return first
        return prev
    except StopIteration:
        return None

if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    result1 = get_middle(data1)
    print(result1)
    data2 = [10, 20, 30, 40]
    result2 = get_middle(data2)
    print(result2)
    data3 = [42]
    result3 = get_middle(data3)
    print(result3)
    data4 = []
    result4 = get_middle(data4)
    print(result4)