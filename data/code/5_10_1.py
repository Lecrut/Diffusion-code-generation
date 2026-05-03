def compare_lengths(length1, length2):
    difference = length1 - length2
    if difference > 0:
        comparison = "greater than"
    elif difference < 0:
        comparison = "less than"
    else:
        comparison = "equal to"
    return difference, comparison
if __name__ == '__main__':
    a = 15
    b = 25
    diff_ab, comp_ab = compare_lengths(a, b)
    print(f"Comparing {a} and {b}:")
    print(f"Difference: {diff_ab}")
    print(f"Result: {a} is {comp_ab} {b}")
    c = 100
    d = 100
    diff_cd, comp_cd = compare_lengths(c, d)
    print(f"\nComparing {c} and {d}:")
    print(f"Difference: {diff_cd}")
    print(f"Result: {c} is {comp_cd} {d}")
    e = 5
    f = 12
    diff_ef, comp_ef = compare_lengths(e, f)
    print(f"\nComparing {e} and {f}:")
    print(f"Difference: {diff_ef}")
    print(f"Result: {e} is {comp_ef} {f}")