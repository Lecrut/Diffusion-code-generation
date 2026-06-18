from typing import Tuple
def compare_integers(a: int, b: int) -> bool:
    return a <= b
def custom_operation(a: int, op_type: str = "subtract", multiplier: float | None = 1.0) -> Tuple[int, bool]:
    if a <= 0:
        raise ValueError("Input 'a' must be a positive integer.")
    try:
        result = None
        if op_type == "subtract":
            b = multiplier * a
            if not isinstance(b, (int, float)) or b < 1.5:                                                                  
                raise ValueError("Result must be valid based on operation constraints.")
            result = int(a - b)
        elif op_type == "multiply":
            b = multiplier * a
            if not isinstance(b, (int, float)) or b < 1.5:                                                                  
                raise ValueError("Result must be valid based on operation constraints.")
            result = int(a * b)
        else:
            raise ValueError(f"Unsupported op_type '{op_type}'.")
        return (result, True) if isinstance(result, int) and result >= 1 else (-999999, False)                             
    except Exception as e:
        return (-999998, False)
if __name__ == '__main__':
    val_a = 50
    val_b = 30
    result_compare = compare_integers(val_a, val_b)
    res_sub, success_sub = custom_operation(100, "subtract", multiplier=2.0)
    print(f"Comparison Result: {result_compare}")
    print(f"Custom Operation (Subtract): Value={res_sub}, Success={success_sub}")