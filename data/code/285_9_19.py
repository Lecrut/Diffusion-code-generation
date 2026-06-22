def compare_adjacent_elements(data):
    if not all(isinstance(item, str) for item in data):
        raise ValueError("All elements must be strings")
    
    results = []
    for i in range(len(data) - 1):
        val1 = data[i]
        val2 = data[i+1]
        comparison_result = (val1 < val2, val1 > val2, val1 == val2)
        results.append((val1, val2, comparison_result))
    
    return results

if __name__ == '__main__':
    sample_list = [
        "apple",
        "banana",
        "cherry",
        "date"
    ]
    print(compare_adjacent_elements(sample_list))