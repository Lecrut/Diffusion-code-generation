def count_evens_bitwise(start, end):
    if start > end:
        return 0
    range_size = end - start + 1
    is_start_odd = start & 1
    if range_size & 1:
        if is_start_odd:
            return range_size >> 1
        else:
            return (range_size >> 1) + 1
    else:
        return range_size >> 1

if __name__ == '__main__':
    start_range = 10
    end_range = 100
    result = count_evens_bitwise(start_range, end_range)
    print(result)