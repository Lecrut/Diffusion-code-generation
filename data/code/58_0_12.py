def count_evens(start, end):
    if start > end:
        return 0
    count_start = start // 2
    count_end = end // 2
    return count_end - count_start

if __name__ == '__main__':
    start_val = 3
    end_val = 10
    result = count_evens(start_val, end_val)
    print(result)