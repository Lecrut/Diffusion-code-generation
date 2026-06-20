def check_boolean_equality(flag1: bool, flag2: bool) -> bool:
    return flag1 == flag2

if __name__ == '__main__':
    sample_values = {
        'True vs True': (True, True),
        'False vs False': (False, False),
        'True vs False': (True, False),
        'False vs True': (False, True)
    }
    
    for description, (flag1, flag2) in sample_values.items():
        result = check_boolean_equality(flag1, flag2)
        print(f'{description}: {result}')