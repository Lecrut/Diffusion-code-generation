def compare_element_counts(structure1, structure2):
    def count_elements(structure):
        if isinstance(structure, list):
            count = 0
            for item in structure:
                count += count_elements(item)
            return count
        elif isinstance(structure, (int, float, str, bool)):
            return 1
        else:
            return 0
    count1 = count_elements(structure1)
    count2 = count_elements(structure2)
    return count1, count2
if __name__ == '__main__':
    data1 = [1, [2, 3], [4, [5, 6]], 7]
    data2 = [1, [2, 3], [4, [5, 6]], 7]
    data3 = [1, [2, 3], [4, [5, 7]], 7]
    count1_a, count2_a = compare_element_counts(data1, data2)
    print(f"Data 1 element count vs Data 2 element count: {count1_a} vs {count2_a}")
    count1_b, count2_b = compare_element_counts(data1, data3)
    print(f"Data 1 element count vs Data 3 element count: {count1_b} vs {count2_b}")