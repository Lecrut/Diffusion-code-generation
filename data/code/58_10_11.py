def count_evens(start, end):
    if start > end:
        return 0
    count_start = (start + 1) // 2
    count_end = end // 2
    return count_end - count_start_start + count_start

def count_evens(start, end):
    if start > end:
        return 0
    return (end // 2) - ((start - 1) // 2)

if __name__ == '__main__':
    start_val = 1
    end_val = 10
    result = count_evens(start_val, end_val)
    print(result)
    start_val2 = 3
    end_val2 = 7
    result2 = count_evens(start_val2, end_val2)
    print(result2)
    start_val3 = -5
    end_val3 = 5
    result3 = count_evens(start_val3, end_val3)
    print(result3)