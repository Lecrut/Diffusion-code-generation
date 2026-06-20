def logical_operations(a: bool, b: bool) -> (bool, bool):
    and_result = a and b
    or_result = a or b
    return (and_result, or_result)

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    and_out, or_out = logical_operations(sample_a, sample_b)
    print(f'AND Result: {and_out}')
    print(f'OR Result: {or_out}')