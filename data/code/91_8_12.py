def negate_boolean(value):
    return not value

if __name__ == '__main__':
    TRUE_VALUE = True
    FALSE_VALUE = False
    
    print(f"Original: {TRUE_VALUE}, Negated: {negate_boolean(TRUE_VALUE)}")
    print(f"Original: {FALSE_VALUE}, Negated: {negate_boolean(FALSE_VALUE)}")