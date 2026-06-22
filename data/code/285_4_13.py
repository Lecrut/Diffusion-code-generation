def compare_consecutive_elements(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise ValueError("Input must be a list or tuple.")
    
    results = []
    for i in range(len(sequence) - 1):
        a, b = sequence[i], sequence[i + 1]
        if a > b:
            results.append('decreasing')
        elif a < b:
            results.append('increasing')
        else:
            results.append('equal')
    
    return results

if __name__ == '__main__':
    sample_data = [10, 5, 5, 20, 30]
    print(compare_consecutive_elements(sample_data))