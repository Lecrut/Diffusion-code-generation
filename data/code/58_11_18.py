def count_evens_between(lower, upper):
    if lower > upper:
        return 0
    first_even = lower if lower % 2 == 0 else lower + 1
    last_even = upper if upper % 2 == 0 else upper - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    result = count_evens_between(1, 10)
    print(result)
    result = count_evens_between(3, 3)
    print(result)
    result = count_evens_between(4, 4)
    print(result)
    result = count_evens_between(5, 5)
    print(result)
    result = count_evens_between(2, 8)
    print(result)
    result = count_evens_between(10, 10)
    print(result)
    result = count_evens_between(11, 11)
    print(result)
    result = count_evens_between(1, 1)
    print(result)
    result = count_evens_between(2, 2)
    print(result)
    result = count_evens_between(0, 0)
    print(result)
    result = count_evens_between(-5, 5)
    print(result)
    result = count_evens_between(-4, 4)
    print(result)