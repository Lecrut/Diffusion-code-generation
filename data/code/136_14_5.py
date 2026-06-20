def short_circuit_and(a: bool, b: bool) -> bool:
    return a and b

def short_circuit_or(a: bool, b: bool) -> bool:
    return a or b

if __name__ == '__main__':
    condition_A = True
    condition_B = False
    
    and_result = short_circuit_and(condition_A, condition_B)
    or_result = short_circuit_or(condition_A, condition_B)
    
    print(f'AND Result: {and_result}')
    print(f'OR Result: {or_result}')