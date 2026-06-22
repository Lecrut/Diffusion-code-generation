def compare_lengths(a, b):
    diff = abs(a - b)
    if a > b:
        desc = "First length is greater"
    elif b > a:
        desc = "Second length is greater"
    else:
        desc = "Both lengths are equal"
    return diff, desc

if __name__ == '__main__':
    length1 = 10.5
    length2 = 7.2
    result = compare_lengths(length1, length2)
    print(result)