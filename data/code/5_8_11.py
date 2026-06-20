def compare_lengths(a, b):
    diff = abs(a - b)
    if a > b:
        description = "first length is greater"
    elif b > a:
        description = "second length is greater"
    else:
        description = "lengths are equal"
    return diff, description

if __name__ == '__main__':
    val1 = 10.5
    val2 = 7.2
    result = compare_lengths(val1, val2)
    print(result)