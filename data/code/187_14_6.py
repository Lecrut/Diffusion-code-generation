class ListAnalyzer:
    def __init__(self, data):
        self._data = data
    def find_maximum(self):
        if not self._data:
            raise ValueError("Cannot find the maximum value in an empty list.")
        maximum = self._data[0]
        for item in self._data[1:]:
            if item > maximum:
                maximum = item
        return maximum
if __name__ == '__main__':
    sample_list_one = [10, 5, 20, 8, 15]
    analyzer_one = ListAnalyzer(sample_list_one)
    try:
        max_val_one = analyzer_one.find_maximum()
        print(f"The maximum value in {sample_list_one} is: {max_val_one}")
    except ValueError as e:
        print(f"Error: {e}")
    sample_list_two = [-5, -1, -10, -2]
    analyzer_two = ListAnalyzer(sample_list_two)
    try:
        max_val_two = analyzer_two.find_maximum()
        print(f"The maximum value in {sample_list_two} is: {max_val_two}")
    except ValueError as e:
        print(f"Error: {e}")
    empty_list = []
    analyzer_empty = ListAnalyzer(empty_list)
    try:
        max_val_empty = analyzer_empty.find_maximum()
        print(f"The maximum value in {empty_list} is: {max_val_empty}")
    except ValueError as e:
        print(f"Error: {e}")