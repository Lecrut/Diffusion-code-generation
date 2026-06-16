def compare_adjacent(data):
    results = []
    for i in range(len(data) - 1):
        a = data[i]
        b = data[i+1]
        if a < b:
            results.append('<')
        elif a > b:
            results.append('>')
        else:
            results.append('=')
    return results
if __name__ == '__main__':
    sample_list = [1, 5, 3, 3, 8, 0]
    comparison_results = compare_adjacent(sample_list)
    print(comparison_results)