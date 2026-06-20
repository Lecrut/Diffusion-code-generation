def compare_elements(data, indices):
    results = []
    for i in range(len(indices) - 1):
        if data[indices[i]] == data[indices[i + 1]]:
            results.append("Equal")
        else:
            results.append("Not Equal")
    return results

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    sample_indices = [0, 2, 3, 4]
    print(compare_elements(sample_data, sample_indices))