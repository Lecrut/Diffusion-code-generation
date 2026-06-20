def evaluate_booleans(boolean_set1, boolean_set2):
    if not all(isinstance(b, bool) for b in boolean_set1) or not all(isinstance(b, bool) for b in boolean_set2):
        raise ValueError("Both inputs must be sets of boolean values.")
    
    intersection = set1 & set2
    union = set1 | set2
    difference = set1 - set2
    
    return intersection, union, difference

if __name__ == '__main__':
    sample_set1 = {True, False, True}
    sample_set2 = {False, True, False}
    intersection, union, difference = evaluate_booleans(sample_set1, sample_set2)
    print("Intersection:", intersection)
    print("Union:", union)
    print("Difference:", difference)