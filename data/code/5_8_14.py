def compare_lengths(a: float, b: float) -> tuple:
    diff = abs(a - b)
    if a > b:
        return diff, "first length is greater"
    elif b > a:
        return diff, "second length is greater"
    else:
        return diff, "lengths are equal"

if __name__ == '__main__':
    result = compare_lengths(5.5, 3.2)
    print(result)