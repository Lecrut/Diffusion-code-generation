def short_circuit_and(a: bool, b: bool) -> bool:
    return a and b

def short_circuit_or(a: bool, b: bool) -> bool:
    return a or b

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    
    and_result = short_circuit_and(sample_a, sample_b)
    or_result = short_circuit_or(sample_a, sample_b)
    
    print(f'AND Result: {and_result}')
    print(f'OR Result: {or_result}')