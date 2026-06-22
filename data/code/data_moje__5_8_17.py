def compare_lengths(a: float, b: float) -> tuple:
    abs_diff = abs(a - b)
    if a > b:
        description = "First length is greater"
    elif b > a:
        description = "Second length is greater"
    else:
        description = "Lengths are equal"
    return abs_diff, description

if __name__ == '__main__':
    result = compare_lengths(10.5, 10.5)
    print(result)