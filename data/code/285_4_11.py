def compare_consecutive_elements(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    
    n = len(sequence)
    if n < 2:
        raise ValueError("Sequence must contain at least two elements")
    
    results = []
    for i in range(n - 1):
        a = sequence[i]
        b = sequence[i + 1]
        if a > b:
            relationship = 'decreasing'
        elif a < b:
            relationship = 'increasing'
        else:
            relationship = 'equal'
        results.append(relationship)
    
    return results

if __name__ == '__main__':
    sample_data = [10, 5, 5, 20, 30]
    print(compare_consecutive_elements(sample_data))