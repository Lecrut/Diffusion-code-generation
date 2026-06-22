def compare_lengths(a, b):
    diff = abs(a - b)
    if a > b:
        desc = "first length is greater"
    elif b > a:
        desc = "second length is greater"
    else:
        desc = "lengths are equal"
    return diff, desc

if __name__ == '__main__':
    result = compare_lengths(5.5, 3.2)
    print(result)
    result = compare_lengths(1.0, 1.0)
    print(result)
    result = compare_lengths(2.3, 7.8)
    print(result)