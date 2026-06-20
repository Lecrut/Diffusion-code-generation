def negate_boolean(value):
    return not value

if __name__ == '__main__':
    TRUE_SAMPLE = True
    FALSE_SAMPLE = False
    
    result1 = negate_boolean(TRUE_SAMPLE)
    print(f"Input: {TRUE_SAMPLE}, Output: {result1}")
    
    result2 = negate_boolean(FALSE_SAMPLE)
    print(f"Input: {FALSE_SAMPLE}, Output: {result2}")