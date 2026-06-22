def count_evens(min_val, max_val):
    if min_val > max_val:
        return 0
    start = min_val if min_val % 2 == 0 else min_val + 1
    if start > max_val:
        return 0
    return (max_val - start) // 2 + 1

if __name__ == '__main__':
    min_val = 10
    max_val = 20
    result = count_evens(min_val, max_val)
    print(result)