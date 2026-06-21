MAX_VALUE_ERROR = "Cannot find maximum of an empty list."

class ListAnalyzer:
    def __init__(self, data):
        self._data = data

    def find_maximum(self):
        if not self._data:
            raise ValueError(MAX_VALUE_ERROR)
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