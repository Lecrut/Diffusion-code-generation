def compare_lengths(a, b):
    diff = abs(a - b)
    if a > b:
        description = f"{a} is greater than {b}"
    elif b > a:
        description = f"{b} is greater than {a}"
    else:
        description = "both are equal"
    return diff, description

if __name__ == '__main__':
    result = compare_lengths(3.14, 2.72)
    print(result)
    result2 = compare_lengths(5.0, 10.5)
    print(result2)
    result3 = compare_lengths(4.2, 4.2)
    print(result3)