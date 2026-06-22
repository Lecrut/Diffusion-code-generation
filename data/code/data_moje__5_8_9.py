def compare_lengths(a: float, b: float):
    diff = abs(a - b)
    if a > b:
        description = f"{a} is greater than {b}"
    elif b > a:
        description = f"{b} is greater than {a}"
    else:
        description = f"{a} is equal to {b}"
    return diff, description

if __name__ == '__main__':
    value1 = 10.5
    value2 = 7.2
    result = compare_lengths(value1, value2)
    print(result)