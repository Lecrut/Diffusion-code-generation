def count_evens(start, end):
    count = 0
    if start % 2 != 0:
        start += 1
    if start <= end:
        count = (end - start) // 2 + 1
    return count

if __name__ == '__main__':
    result = count_evens(1, 10)
    print(result)
    result = count_evens(5, 15)
    print(result)
    result = count_evens(0, 0)
    print(result)
    result = count_evens(3, 3)
    print(result)