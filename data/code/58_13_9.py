def count_even(start, stop):
    if start > stop:
        return 0
    first = start if start % 2 == 0 else start + 1
    last = stop if stop % 2 == 0 else stop - 1
    if first > last:
        return 0
    return (last - first) // 2 + 1

if __name__ == '__main__':
    result = count_even(1, 10)
    print(result)