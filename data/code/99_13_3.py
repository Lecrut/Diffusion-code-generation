def process_flags(flag_a, flag_b, operator):
    if operator == 'and':
        return flag_a and flag_b
    elif operator == 'or':
        return flag_a or flag_b
    else:
        raise ValueError('Unsupported operator')
if __name__ == '__main__':
    print(process_flags(True, False, 'and'))
    print(process_flags(True, True, 'or'))