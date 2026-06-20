def compare_lengths(a, b):
    diff = abs(a - b)
    if a > b:
        result = f"First length {a} is greater than second length {b}"
    elif b > a:
        result = f"Second length {b} is greater than first length {a}"
    else:
        result = f"Both lengths {a} are equal"
    return diff, result

if __name__ == '__main__':
    val1 = 10.5
    val2 = 7.2
    diff, description = compare_lengths(val1, val2)
    print(diff)
    print(description)