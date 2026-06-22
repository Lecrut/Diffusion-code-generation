def compare_lengths(a: float, b: float) -> tuple:
    diff = abs(a - b)
    if a > b:
        description = f"{a} is greater"
    elif b > a:
        description = f"{b} is greater"
    else:
        description = "Both are equal"
    return (diff, description)

if __name__ == '__main__':
    result = compare_lengths(10.5, 7.2)
    print(result)
    result2 = compare_lengths(3.14, 3.14)
    print(result2)
    result3 = compare_lengths(1.0, 5.0)
    print(result3)