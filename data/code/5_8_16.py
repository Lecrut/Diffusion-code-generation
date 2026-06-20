def compare_lengths(a: float, b: float) -> tuple:
    diff = abs(a - b)
    if a > b:
        description = "first is greater"
    elif b > a:
        description = "second is greater"
    else:
        description = "equal"
    return (diff, description)

if __name__ == '__main__':
    result = compare_lengths(3.14, 2.71)
    print(result)
    result2 = compare_lengths(5.0, 5.0)
    print(result2)
    result3 = compare_lengths(1.0, 10.0)
    print(result3)