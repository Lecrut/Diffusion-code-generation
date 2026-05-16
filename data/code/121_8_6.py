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
    data3 = [1, [2, 3], [4, [5, 6]], 8]
    count_a, count_b = compare_element_counts(data1, data2)
    print(f"Data 1 element count: {count_a}")
    print(f"Data 2 element count: {count_b}")
    print(f"Are Data 1 and Data 2 counts equal? {count_a == count_b}")
    count_a, count_c = compare_element_counts(data1, data3)
    print(f"Data 1 element count: {count_a}")
    print(f"Data 3 element count: {count_c}")
    print(f"Are Data 1 and Data 3 counts equal? {count_a == count_c}")