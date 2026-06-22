def count_evens_in_range(start, stop):
    if start >= stop:
        return 0
    length = stop - start
    count = length // 2
    if length % 2 == 1:
        if start % 2 == 0:
            count += 1
    return count

if __name__ == '__main__':
    start_val = 1
    end_val = 10
    result = count_evens_in_range(start_val, end_val)
    print(result)