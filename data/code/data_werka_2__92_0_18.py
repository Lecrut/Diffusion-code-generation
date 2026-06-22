TRUE_VAL = True
FALSE_VAL = False

def invert_truth(state):
    if state is TRUE_VAL:
        return FALSE_VAL
    if state is FALSE_VAL:
        return TRUE_VAL
    raise ValueError("Expected boolean")

if __name__ == '__main__':
    original = True
    result = invert_truth(original)
    print(result)
    result2 = invert_truth(False)
    print(result2)