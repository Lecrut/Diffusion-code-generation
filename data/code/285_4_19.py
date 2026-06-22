def compare_consecutive_elements(sequence):
    results = []
    n = len(sequence)
    for i in range(n - 1):
        if sequence[i] > sequence[i + 1]:
            results.append('decreasing')
        elif sequence[i] < sequence[i + 1]:
            results.append('increasing')
        else:
            results.append('equal')
    return results

if __name__ == '__main__':
    sample_data = [10, 5, 5, 20, 30]
    print(compare_consecutive_elements(sample_data))