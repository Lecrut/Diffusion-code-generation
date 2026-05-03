def compare_lengths(length1, length2):
    difference = length1 - length2
    if difference > 0:
        comparison_result = "greater than"
    elif difference < 0:
        comparison_result = "less than"
    else:
        comparison_result = "equal to"
    return difference, comparison_result
if __name__ == '__main__':
    a = 25
    b = 15
    diff_ab, result_ab = compare_lengths(a, b)
    print(f"Comparing {a} and {b}: Difference = {diff_ab}, Result = {result_ab}")
    c = 100
    d = 100
    diff_cd, result_cd = compare_lengths(c, d)
    print(f"Comparing {c} and {d}: Difference = {diff_cd}, Result = {result_cd}")
    e = 5
    f = 20
    diff_ef, result_ef = compare_lengths(e, f)
    print(f"Comparing {e} and {f}: Difference = {diff_ef}, Result = {result_ef}")