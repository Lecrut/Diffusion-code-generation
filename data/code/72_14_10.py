class ElementComparator:
    POSITION_TO_COMPARE = 1

    @staticmethod
    def count_matching_elements(array1, array2):
        return sum(1 for i in range(min(len(array1), len(array2))) if array1[i] == array2[i])

if __name__ == '__main__':
    sample_array1 = [1, 2, 3, 4, 5]
    sample_array2 = [1, 2, 4, 4, 6]
    matching_count = ElementComparator.count_matching_elements(sample_array1, sample_array2)
    print(matching_count)