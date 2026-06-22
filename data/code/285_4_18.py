def compare_consecutive_elements(sequence):
    results = []
    for i in range(len(sequence) - 1):
        if sequence[i] < sequence[i + 1]:
            results.append('increasing')
        elif sequence[i] > sequence[i + 1]:
            results.append('decreasing')
        else:
            results.append('equal')
    return results

if __name__ == '__main__':
    sample_sequence = [10, 5, 5, 20, 30]
    print(compare_consecutive_elements(sample_sequence))