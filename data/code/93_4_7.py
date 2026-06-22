def determine_both_false(val1, val2):
    try:
        bool1 = bool(val1)
    except Exception:
        bool1 = False
    
    try:
        bool2 = bool(val2)
    except Exception:
        bool2 = False
    
    return not bool1 and not bool2

if __name__ == '__main__':
    result = determine_both_false(False, False)
    print(result)