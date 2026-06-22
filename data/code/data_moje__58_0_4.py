def count_evens(start, end):
    if start > end:
        return 0
    return (end // 2) - ((start - 1) // 2)

if __name__ == '__main__':
    result = count_evens(1, 10)
    print(result)
    result = count_evens(4, 4)
    print(result)
    result = count_evens(5, 5)
    print(result)
    result = count_evens(-5, 5)
    print(result)