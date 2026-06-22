def count_evens(start, end):
    count = 0
    current = start
    while current <= end:
        if current % 2 == 0:
            count += 1
        current += 1
    return count

if __name__ == '__main__':
    result = count_evens(1, 100)
    print(result)
    result2 = count_evens(10, 20)
    print(result2)
    result3 = count_evens(5, 5)
    print(result3)