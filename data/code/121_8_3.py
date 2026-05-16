def compare_element_counts(data1, data2):
    def count_elements(data):
        count = 0
        if isinstance(data, list):
            for item in data:
                if isinstance(item, list):
                    count += count_elements(item)
                else:
                    count += 1
        return count
    count1 = count_elements(data1)
    count2 = count_elements(data2)
    return count1, count2
if __name__ == '__main__':
    structure1 = [1, [2, 3], [4, [5, 6]], 7]
    structure2 = [1, [2, 3], [4, [5, 6]], 7]
    structure3 = [1, [2, 3], [4, [5, 6]], 8]
    structure4 = [1, [2, 3], [4, [5, 6]]]
    c1, c2 = compare_element_counts(structure1, structure2)
    print(f"Structure 1 element count: {c1}")
    print(f"Structure 2 element count: {c2}")
    print(f"Are structure 1 and 2 equal? {c1 == c2}")
    c1, c3 = compare_element_counts(structure1, structure3)
    print(f"Structure 1 element count: {c1}")
    print(f"Structure 3 element count: {c3}")
    print(f"Are structure 1 and 3 equal? {c1 == c3}")
    c1, c4 = compare_element_counts(structure1, structure4)
    print(f"Structure 1 element count: {c1}")
    print(f"Structure 4 element count: {c4}")
    print(f"Are structure 1 and 4 equal? {c1 == c4}")