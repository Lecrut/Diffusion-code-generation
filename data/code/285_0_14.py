class ElementComparator:
    INCREASING = "increasing"
    DECREASING = "decreasing"
    EQUAL = "equal"

    @staticmethod
    def compare_adjacent(data):
        results = []
        for i in range(len(data) - 1):
            a = data[i]
            b = data[i+1]
            if a > b:
                results.append(ElementComparator.DECREASING)
            elif a < b:
                results.append(ElementComparator.INCREASING)
            else:
                results.append(ElementComparator.EQUAL)
        return results

if __name__ == '__main__':
    sample_data = [1, 5, 2, 8, 8, 3]
    comparison_results = ElementComparator.compare_adjacent(sample_data)
    print(comparison_results)