class StringComparator:
    ASCENDING = 'ascending'
    DESCENDING = 'descending'
    EQUAL = 'equal'

    @staticmethod
    def compare_adjacent_elements(data):
        results = []
        for i in range(len(data) - 1):
            val1, val2 = data[i], data[i + 1]
            if val1 < val2:
                result = StringComparator.ASCENDING
            elif val1 > val2:
                result = StringComparator.DESCENDING
            else:
                result = StringComparator.EQUAL
            results.append((val1, val2, result))
        return results

if __name__ == '__main__':
    sample_list = [
        "apple",
        "banana",
        "cherry",
        "date"
    ]
    print("Comparing adjacent strings:")
    comparison_results = StringComparator.compare_adjacent_elements(sample_list)
    for result in comparison_results:
        print(result)