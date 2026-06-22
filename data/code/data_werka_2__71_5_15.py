def get_middle_element(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return
    low = first
    high = first
    step = 0
    for item in iterator:
        step += 1
        high = item
        if step % 2 == 0:
            try:
                low = next(iterator)
            except StopIteration:
                yield high
                return
        else:
            yield high
            return
    if step % 2 == 0:
        yield high
    else:
        yield low

if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    result1 = get_middle_element(data1)
    print(result1)
    data2 = [10, 20, 30, 40]
    result2 = get_middle_element(data2)
    print(result2)
    data3 = [100]
    result3 = get_middle_element(data3)
    print(result3)
    data4 = []
    result4 = get_middle_element(data4)
    print(result4)
    data5 = [1, 2]
    result5 = get_middle_element(data5)
    print(result5)
    data6 = [1, 2, 3]
    result6 = get_middle_element(data6)
    print(result6)