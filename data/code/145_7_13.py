def evaluate_expression(flags):
    if flags['flag1']:
        if flags['flag2']:
            return True
        elif not flags['flag3']:
            return False
    else:
        if flags['flag4']:
            return True
        elif flags['flag5'] and flags['flag6']:
            return False
    return False

if __name__ == '__main__':
    sample_flags = {
        'flag1': True,
        'flag2': False,
        'flag3': True,
        'flag4': False,
        'flag5': True,
        'flag6': False
    }
    print(evaluate_expression(sample_flags))