class ArrayComparator:
    def check_adjacencies(self, numbers):
        result = []
        for index in range(len(numbers) - 1):
            first_element = numbers[index]
            second_element = numbers[index + 1]
            comparison_tuple = (first_element, second_element)
            result.append(comparison_tuple)
        return result

if __name__ == '__main__':
    SAMPLE_LIST = [4, 9, 1, 6, 7]
    comparator_instance = ArrayComparator()
    adjacency_results = comparator_instance.check_adjacencies(SAMPLE_LIST)
    print(adjacency_results)