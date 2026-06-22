import numpy as np

class ElementComparator:
    INCREASING = 'increasing'
    DECREASING = 'decreasing'
    EQUAL = 'equal'

    @staticmethod
    def compare_consecutive_elements(arr):
        results = []
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                results.append(ElementComparator.INCREASING)
            elif arr[i] > arr[i + 1]:
                results.append(ElementComparator.DECREASING)
            else:
                results.append(ElementComparator.EQUAL)
        return results

if __name__ == '__main__':
    sample_array = np.array([1, 2, 3, 2, 1])
    comparator = ElementComparator()
    result = comparator.compare_consecutive_elements(sample_array)
    print(result)