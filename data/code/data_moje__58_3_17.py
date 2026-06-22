def count_evens(start, end):
    if start > end:
        return 0
    count_start = start // 2
    count_end = end // 2
    return count_end - count_start + (1 if start % 2 == 0 else 0)

if __name__ == '__main__':
    result = count_evens(3, 15)
    print(result)