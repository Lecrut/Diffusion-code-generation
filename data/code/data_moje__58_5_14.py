def count_even(start, end):
    if start > end:
        return 0
    adjusted_start = start if start % 2 == 0 else start + 1
    if adjusted_start > end:
        return 0
    count = (end - adjusted_start) // 2 + 1
    return count

if __name__ == '__main__':
    result = count_even(1, 10)
    print(result)
    result2 = count_even(2, 10)
    print(result2)
    result3 = count_even(1, 1)
    print(result3)
    result4 = count_even(10, 10)
    print(result4)
    result5 = count_even(5, 1)
    print(result5)