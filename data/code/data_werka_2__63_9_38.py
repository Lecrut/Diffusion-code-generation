class ListAnalyzer:
    def __init__(self, lst):
        self.lst = lst

    def find_first_value(self):
        if not self.lst:
            raise ValueError("The list is empty")
        return self.lst[0]

if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        ['apple', 'banana', 'cherry'],
        [True, False],
        []
    ]

    for data in sample_data:
        analyzer = ListAnalyzer(data)
        try:
            first_value = analyzer.find_first_value()
            print(f"First value: {first_value}")
        except ValueError as e:
            print(e)