TRUE = 'True'
FALSE = 'False'

def get_opposite(value):
    if value.lower() == TRUE:
        return FALSE
    elif value.lower() == FALSE:
        return TRUE
    else:
        raise ValueError('Invalid boolean value')
if __name__ == '__main__':
    sample1 = 'True'
    sample2 = 'False'
    print(f'Opposite of {sample1}: {get_opposite(sample1)}')
    print(f'Opposite of {sample2}: {get_opposite(sample2)}')