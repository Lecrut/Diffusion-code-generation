def compare_lengths(a, b):
    diff = abs(a - b)
    if a > b:
        desc = "first is greater"
    elif b > a:
        desc = "second is greater"
    else:
        desc = "both are equal"
    return diff, desc

if __name__ == '__main__':
    result = compare_lengths(5.5, 3.2)
    print(result)
    result = compare_lengths(10.0, 10.0)
    print(result)
    result = compare_lengths(2.1, 8.9)
    print(result)