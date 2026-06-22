def count_evens(start, end):
    count_start = (start + 1) // 2
    count_end = end // 2
    return count_end - count_start + (1 if start % 2 == 0 else 0)

if __name__ == '__main__':
    result = count_evens(1, 10)
    print(result)