from typing import Tuple

TRUE_CONST: int = 1
FALSE_CONST: int = 0
BINARY_MASK: int = 0x01

def check_logic(A: bool, B: bool, C: bool) -> bool:
    not_c: bool = (C is False)
    b_or_not_c: bool = (B is True) or not_c
    final_result: bool = (A is True) and b_or_not_c
    return final_result

def _compute_binary_weight(val: bool) -> int:
    if val:
        return TRUE_CONST
    return FALSE_CONST

if __name__ == '__main__':
    a_input: bool = True
    b_input: bool = False
    c_input: bool = True
    
    step_not_c: bool = (c_input is False)
    step_b_or_not_c: bool = (b_input is True) or step_not_c
    step_and: bool = (a_input is True) and step_b_or_not_c
    
    weight_a: int = _compute_binary_weight(a_input)
    weight_b: int = _compute_binary_weight(b_input)
    weight_c: int = _compute_binary_weight(c_input)
    
    combined: int = (weight_a << 2) | (weight_b << 1) | weight_c
    mask_check: int = combined & BINARY_MASK
    
    final_val: bool = (mask_check == BINARY_MASK) if (weight_a == TRUE_CONST) else (mask_check == FALSE_CONST)
    
    print(final_val)