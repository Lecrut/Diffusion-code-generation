class ListAnalyzer:
    def __init__(self, data):
        self._data = data
    def find_maximum(self):
        if not self._data:
            raise ValueError("Cannot find the maximum value in an empty list.")
        maximum_value = self._data[0]
        for value in self._data[1:]:
            if value > maximum_value:
                maximum_value = value
        return maximum_value
if __name__ == '__main__':
    sample_list_one = [10, 5, 20, 8, 15]
    analyzer_one = ListAnalyzer(sample_list_one)
    try:
        max_one = analyzer_one.find_maximum()
        print(f"The maximum value in {sample_list_one} is: {max_one}")
    except ValueError as e:
        print(f"Error: {e}")
    sample_list_two = [3, 9, 1, 5]
    analyzer_two = ListAnalyzer(sample_list_two)
    try:
        max_two = analyzer_two.find_maximum()
        print(f"The maximum value in {sample_list_two} is: {max_two}")
    except ValueError as e:
        print(f"Error: {e}")
    sample_list_empty = []
    analyzer_empty = ListAnalyzer(sample_list_empty)
    try:
        max_empty = analyzer_empty.find_maximum()
        print(f"The maximum value in {sample_list_empty} is: {max_empty}")
    except ValueError as e:
        print(f"Error: {e}")