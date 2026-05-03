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
    b = 10
    diff_ab, comp_ab = compare_lengths(a, b)
    print(f"Comparing {a} and {b}: Difference = {diff_ab}, Result = {comp_ab}")
    c = 20
    d = 20
    diff_cd, comp_cd = compare_lengths(c, d)
    print(f"Comparing {c} and {d}: Difference = {diff_cd}, Result = {comp_cd}")
    e = 5
    f = 12
    diff_ef, comp_ef = compare_lengths(e, f)
    print(f"Comparing {e} and {f}: Difference = {diff_ef}, Result = {comp_ef}")