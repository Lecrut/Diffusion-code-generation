OUTCOME_GREATER = 'greater than'
OUTCOME_LESS = 'less than'
OUTCOME_EQUAL = 'equal to'

def compare_integers(a, b):
    if a > b:
        return OUTCOME_GREATER
    elif a < b:
        return OUTCOME_LESS
    else:
        return OUTCOME_EQUAL
if __name__ == '__main__':
    result = compare_integers(10, 5)
    print(result)