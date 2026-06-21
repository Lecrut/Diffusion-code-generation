class ListAnalyzer:
    def __init__(self, data):
        self.data = data

    def find_smallest(self):
        if not self.data:
            raise ValueError("Input list cannot be empty")
        sorted_data = sorted(self.data)
        return sorted_data[0]

if __name__ == '__main__':
    analyzer = ListAnalyzer([3.14, -1.5, 2.718, -10.0, 0.5, 42.0])
    try:
        result = analyzer.find_smallest()
        print(result)
    except ValueError as e:
        print(f"Error: {e}")