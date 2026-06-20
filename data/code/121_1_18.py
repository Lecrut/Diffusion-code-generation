def compare_floats(a, b):
    tolerance = 1e-9
    diff = abs(a - b)
    if diff < tolerance:
        return (a, "equal")
    elif a > b:
        return (a, "greater than b")
    else:
        return (b, "greater than a")

if __name__ == '__main__':
    sample1_a = 0.1 + 0.2
    sample1_b = 0.3
    result1 = compare_floats(sample1_a, sample1_b)
    print(result1)

    sample2_a = 0.75 - 0.25
    sample2_b = 0.5
    result2 = compare_floats(sample2_a, sample2_b)
    print(result2)