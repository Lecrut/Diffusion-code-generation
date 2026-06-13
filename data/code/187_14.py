class ListAnalyzer:
    def __init__(self, data):
        self._data = data
    def find_maximum(self):
        if not self._data:
            raise ValueError("Cannot find maximum of an empty list.")
        return max(self._data)
if __name__ == '__main__':
    sample_list_one = [10, 5, 20, 8]
    analyzer_one = ListAnalyzer(sample_list_one)
    try:
        max_val_one = analyzer_one.find_maximum()
        print(f"Maximum value in {sample_list_one}: {max_val_one}")
    except ValueError as e:
        print(f"Error for sample list one: {e}")
    sample_list_two = [-5, -1, -10]
    analyzer_two = ListAnalyzer(sample_list_two)
    try:
        max_val_two = analyzer_two.find_maximum()
        print(f"Maximum value in {sample_list_two}: {max_val_two}")
    except ValueError as e:
        print(f"Error for sample list two: {e}")
    empty_list = []
    analyzer_empty = ListAnalyzer(empty_list)
    try:
        max_val_empty = analyzer_empty.find_maximum()
        print(f"Maximum value in empty list: {max_val_empty}")
    except ValueError as e:
        print(f"Error for empty list: {e}")