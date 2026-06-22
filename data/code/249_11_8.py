class ListAnalyzer:
    def __init__(self, data):
        self.data = data

    def find_largest(self):
        if not self.data:
            raise ValueError("Input list cannot be empty")
        largest = self.data[0]
        for number in self.data[1:]:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    analyzer1 = ListAnalyzer([1, 5, 2, 8, 3])
    analyzer2 = ListAnalyzer([-10, -5, -20, -1])
    analyzer3 = ListAnalyzer([42])
    empty_list_analyzer = ListAnalyzer([])
    
    print(f"Largest in {analyzer1.data}: {analyzer1.find_largest()}")
    print(f"Largest in {analyzer2.data}: {analyzer2.find_largest()}")
    print(f"Largest in {analyzer3.data}: {analyzer3.find_largest()}")
    try:
        empty_list_analyzer.find_largest()
    except ValueError as e:
        print(e)