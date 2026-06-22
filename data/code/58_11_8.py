def count_evens(a, b):
    if a > b:
        return 0
    start = (a + 1) // 2
    end = b // 2
    return max(0, end - start + 1)

if __name__ == '__main__':
    lower_bound = 5
    upper_bound = 20
    result = count_evens(lower_bound, upper_bound)
    print(result)