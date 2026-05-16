def compare_element_counts(structure1, structure2):
    def count_elements(structure):
        count = 0
        if isinstance(structure, list):
            for item in structure:
                count += count_elements(item)
        elif isinstance(structure, (int, float, str, bool)):
            count += 1
        return count
    count1 = count_elements(structure1)
    count2 = count_elements(structure2)
    return count1 == count2
if __name__ == '__main__':
    data1 = [1, [2, 3], [4, [5, 6]], 7]
    data2 = [1, [2, 3], [4, [5, 6]], 7]
    data3 = [1, [2, 3], [4, [5, 7]], 7]
    data4 = [1, [2, 3], [4, [5, 6]], 8]
    print(f"Comparing data1 and data2: {compare_element_counts(data1, data2)}")
    print(f"Comparing data1 and data3: {compare_element_counts(data1, data3)}")
    print(f"Comparing data1 and data4: {compare_element_counts(data1, data4)}")