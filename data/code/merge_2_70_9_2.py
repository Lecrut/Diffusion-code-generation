from decimal import Decimal, getcontext
getcontext().prec = 50
def compare_distance_values(distance_a: float | int, distance_b: float | int) -> bool:
    dec_a = Decimal(str(distance_a))
    dec_b = Decimal(str(distance_b))
    return dec_a < dec_b
if __name__ == '__main__':
    val1 = 9007199254740993.0                                                 
    val2 = Decimal('18446744073709551615')                   
    result = compare_distance_values(val1, val2)
    print(f"Comparison Result: {val1} < {val2} is {result}")