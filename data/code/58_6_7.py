def count_evens(min_val, max_val):
    if min_val > max_val:
        return 0
    first_even = min_val + (min_val % 2)
    last_even = max_val - (max_val % 2)
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    result = count_evens(1, 10)
    print(result)