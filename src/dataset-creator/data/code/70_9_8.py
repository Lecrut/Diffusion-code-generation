from decimal import Decimal, getcontext
getcontext().prec = 50
def compare_distances(distance_a: str, distance_b: str) -> int:
    val_a = Decimal(distance_a)
    val_b = Decimal(distance_b)
    return -1 if val_a < val_b else (0 if val_a == val_b else 1)
if __name__ == '__main__':
    d_large_1 = "9223372036854775807"                             
    d_small_1 = "100"
    result_a_b = compare_distances(d_large_1, d_small_1)
    print(f"Comparison of {d_large_1} and {d_small_1}: Result is {'less' if result_a_b == -1 else 'equal' if result_a_b == 0 else 'greater'}")
    d_equal = "12345678901234567890" * 10
    res_same = compare_distances(d_equal, d_equal)
    print(f"Comparison of two identical large strings: Result is {'less' if res_same == -1 else 'equal' if res_same == 0 else 'greater'}")
    d_larger = "9" + ("8" * 50)
    d_smaller = "1" + ("2" * 60)
    res_diff = compare_distances(d_larger, d_smaller)
    print(f"Comparison of {d_larger} and {d_smaller}: Result is {'less' if res_diff == -1 else 'equal' if res_diff == 0 else 'greater'}")