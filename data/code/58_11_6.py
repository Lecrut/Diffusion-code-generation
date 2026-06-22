def count_evens_between(lower, upper):
    if lower > upper:
        return 0
    count_up_to = lambda n: (n // 2) + 1 if n >= 0 else -((-n + 1) // 2)
    return count_up_to(upper) - count_up_to(lower - 1)

if __name__ == '__main__':
    start = 3
    end = 10
    result = count_evens_between(start, end)
    print(result)