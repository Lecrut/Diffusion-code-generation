def check_complex_condition(a, b, c, d):
    conditions = {
        'a_and_b': a and b,
        'c_or_d': c or d,
        'not_a': not a,
        'b_xor_c': b ^ c,
        'd_nand_a': not (d and a)
    }
    return all(conditions.values())

if __name__ == '__main__':
    sample_values = {
        'a': True, 'b': False, 'c': True, 'd': False
    }
    result = check_complex_condition(**sample_values)
    print(result)