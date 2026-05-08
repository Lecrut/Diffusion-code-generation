class ListAnalyzer:
    def __init__(self):
        self.data = None
    def set_list(self, data):
        self.data = data
    def get_largest(self):
        if self.data is None:
            raise ValueError("No list has been set.")
        if not self.data:
            raise ValueError("The list is empty.")
        return max(self.data)
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_list_1 = [10, 5, 20, 8, 15]
    sample_list_2 = [-5, -1, -10, -2]
    sample_list_3 = [3.14, 2.71, 1.618]
    sample_list_empty = []
    analyzer.set_list(sample_list_1)
    print(f"Largest in {sample_list_1}: {analyzer.get_largest()}")
    analyzer.set_list(sample_list_2)
    print(f"Largest in {sample_list_2}: {analyzer.get_largest()}")
    analyzer.set_list(sample_list_3)
    print(f"Largest in {sample_list_3}: {analyzer.get_largest()}")
    try:
        analyzer.set_list(sample_list_empty)
        analyzer.get_largest()
    except ValueError as e:
        print(f"Error for empty list: {e}")