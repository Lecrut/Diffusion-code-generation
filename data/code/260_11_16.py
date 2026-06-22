class MaxNumberFinder:
    def find_max_in_sets(self, sets):
        return {key: max(value) for key, value in sets.items()}

if __name__ == '__main__':
    finder = MaxNumberFinder()
    sample_sets = {
        'set1': [3, 5, 2],
        'set2': [8, 1, 9],
        'set3': [4, 6, 7]
    }
    max_values = finder.find_max_in_sets(sample_sets)
    print(max_values)