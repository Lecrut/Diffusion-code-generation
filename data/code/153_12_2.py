class ListChecker:
    def __init__(self, initial_list):
        self._data = list(initial_list)
    def contains(self, element):
        return element in self._data
if __name__ == '__main__':
    sample_list = [1, 5, 10, 15, 20]
    checker = ListChecker(sample_list)
    element_to_find_1 = 10
    element_to_find_2 = 100
    result_1 = checker.contains(element_to_find_1)
    result_2 = checker.contains(element_to_find_2)
    print(f"List: {sample_list}")
    print(f"Checking for {element_to_find_1}: {result_1}")
    print(f"Checking for {element_to_find_2}: {result_2}")