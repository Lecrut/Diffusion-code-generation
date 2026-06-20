def logical_combinations(flag_a: bool, flag_b: bool, operator: str) -> bool:
    if operator == 'and':
        return flag_a and flag_b
    elif operator == 'or':
        return flag_a or flag_b
    else:
        raise ValueError('Invalid operator')
if __name__ == '__main__':
    print(logical_combinations(True, False, 'and'))
    print(logical_combinations(True, True, 'or'))