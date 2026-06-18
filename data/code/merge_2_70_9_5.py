from decimal import Decimal, getcontext
getcontext().prec = 50
def normalize_distance(value: int) -> float:
    if not isinstance(value, int) or value < 0:
        raise ValueError("Distance must be a non-negative integer.")
    dec_value = Decimal(str(value))
    return float(dec_value)
def compare_distances(a: int, b: int) -> str:
    norm_a = normalize_distance(a)
    norm_b = normalize_distance(b)
    if norm_a > norm_b:
        return "a_is_greater"
    elif norm_b > norm_a:
        return "b_is_greater"
    else:
        return "equal"
if __name__ == '__main__':
    val1 = 9007199254740993                                 
    val2 = 10**50                               
    result = compare_distances(val1, val2)
    print(f"Comparing {val1} and {val2}:")
    print(result)