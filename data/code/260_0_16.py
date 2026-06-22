def compare_sets(set1, set2):
    if not all(isinstance(x, (int, float)) for x in set1) or not all(isinstance(x, (int, float)) for x in set2):
        raise ValueError("Both sets must contain only numbers.")
    
    larger = [x for x in set1 if x > max(set2)] + [y for y in set2 if y > max(set1)]
    return larger

if __name__ == '__main__':
    sample_set1 = {5, 3, 9, 7}
    sample_set2 = {4, 6, 8, 10}
    result = compare_sets(sample_set1, sample_set2)
    print(result)