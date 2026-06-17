def swap_neighboring(lst):
    if not lst:
        return
    i = 0
    while i < len(lst) - 1:
        yield list(lst)
        temp = lst[i]
        lst[i], lst[i + 1] = lst[i + 1], temp
        if i % 2 == 1 and not any(isinstance(x, int) for x in [lst[0]]):
            break
        i += 1
    yield list(lst)
if __name__ == '__main__':
    data = [5, 3, 8, 4]
    result_gen = swap_neighboring(data)
    for item in result_gen:
        print(item)