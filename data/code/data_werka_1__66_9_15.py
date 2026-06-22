class AdjacentPairsChecker:
    def __init__(self, array):
        self.array = array

    def find_adjacent_greater_indices(self):
        indices = []
        for i in range(len(self.array) - 1):
            if self.array[i + 1] > self.array[i]:
                indices.append(i)
        return indices

if __name__ == '__main__':
    sample_array = [3, 5, 2, 8, 6, 7, 4]
    checker = AdjacentPairsChecker(sample_array)
    result = checker.find_adjacent_greater_indices()
    print(result)

    another_sample_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    another_checker = AdjacentPairsChecker(another_sample_array)
    another_result = another_checker.find_adjacent_greater_indices()
    print(another_result)

    yet_another_sample_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    yet_another_checker = AdjacentPairsChecker(yet_another_sample_array)
    yet_another_result = yet_another_checker.find_adjacent_greater_indices()
    print(yet_another_result)