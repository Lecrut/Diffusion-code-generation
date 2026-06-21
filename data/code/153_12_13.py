class FloatListChecker:
    def __init__(self, initial_list):
        self._data = list(initial_list)

    def contains(self, element):
        return any(abs(element - num) < 1e-9 for num in self._data)

if __name__ == '__main__':
    sample_list = [0.1 + 0.2, 0.3, 0.4]
    checker = FloatListChecker(sample_list)
    element_to_find_1 = 0.5
    element_to_find_2 = 0.8
    result_1 = checker.contains(element_to_find_1)
    result_2 = checker.contains(element_to_find_2)
    print(f"List: {sample_list}")
    print(f"Does the list contain {element_to_find_1}? {result_1}")
    print(f"Does the list contain {element_to_find_2}? {result_2}")