def middle_element_generator(iterable):
    try:
        iterator = iter(iterable)
        first = next(iterator)
        second = next(iterator)
    except StopIteration:
        return

    if not first and not second:
        if not first and not second:
            yield second
            return

    prev = first
    curr = second
    count = 2

    for item in iterator:
        prev = curr
        curr = item
        count += 1

    if count % 2 == 1:
        yield curr
    else:
        yield prev

if __name__ == '__main__':
    data1 = [10, 20, 30, 40, 50]
    gen1 = middle_element_generator(data1)
    print(list(gen1))

    data2 = [100, 200, 300, 400]
    gen2 = middle_element_generator(data2)
    print(list(gen2))

    data3 = [42]
    gen3 = middle_element_generator(data3)
    print(list(gen3))