class ListAnalyzer:
    def __init__(self, data):
        self._data = data
    def find_maximum(self):
        if not self._data:
            raise ValueError("The list is empty, cannot find the maximum value.")
        return max(self._data)
if __name__ == '__main__':
    sample_list_one = [10, 5, 20, 8]
    analyzer_one = ListAnalyzer(sample_list_one)
    try:
        max_val_one = analyzer_one.find_maximum()
        print(f"The maximum value in {sample_list_one} is: {max_val_one}")
    except ValueError as e:
        print(f"Error: {e}")
    sample_list_two = [3, 9, 1, 5]
    analyzer_two = ListAnalyzer(sample_list_two)
    try:
        max_val_two = analyzer_two.find_maximum()
        print(f"The maximum value in {sample_list_two} is: {max_val_two}")
    except ValueError as e:
        print(f"Error: {e}")
    sample_list_empty = []
    analyzer_empty = ListAnalyzer(sample_list_empty)
    try:
        max_val_empty = analyzer_empty.find_maximum()
        print(f"The maximum value in {sample_list_empty} is: {max_val_empty}")
    except ValueError as e:
        print(f"Error: {e}")