def compare_lengths(a, b):
    diff = abs(a - b)
    if a > b:
        description = "The first length is greater"
    elif b > a:
        description = "The second length is greater"
    else:
        description = "Both lengths are equal"
    return diff, description

if __name__ == '__main__':
    val1 = 10.5
    val2 = 7.2
    result = compare_lengths(val1, val2)
    print(result)