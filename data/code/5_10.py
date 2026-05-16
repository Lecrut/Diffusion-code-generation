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
    print(f"Difference (a - b): {diff_ab}")
    print(f"{a} is {comp_ab} {b}")
    c = 10
    d = 10
    diff_cd, comp_cd = compare_lengths(c, d)
    print(f"\nComparing {c} and {d}:")
    print(f"Difference (c - d): {diff_cd}")
    print(f"{c} is {comp_cd} {d}")
    e = 30
    f = 10
    diff_ef, comp_ef = compare_lengths(e, f)
    print(f"\nComparing {e} and {f}:")
    print(f"Difference (e - f): {diff_ef}")
    print(f"{e} is {comp_ef} {f}")