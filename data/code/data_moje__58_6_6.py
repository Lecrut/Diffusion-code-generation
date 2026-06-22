def count_evens(min_val, max_val):
    if min_val > max_val:
        return 0
    count = 0
    count += (max_val // 2) - ((min_val - 1) // 2)
    return count

if __name__ == '__main__':
    min_val = 3
    max_val = 10
    result = count_evens(min_val, max_val)
    print(result)