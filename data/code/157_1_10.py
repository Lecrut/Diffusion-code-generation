class ListAnalyzer:
    def __init__(self, data):
        self.data = data

    def find_smallest(self):
        return min(self.data)

if __name__ == '__main__':
    analyzer1 = ListAnalyzer([3, 1, 4, 1, 5, 9, 2])
    analyzer2 = ListAnalyzer([-10, 0, 5, -20, 100])
    analyzer3 = ListAnalyzer([7])
    empty_analyzer = ListAnalyzer([])
    
    print(f"Smallest in {analyzer1.data}: {analyzer1.find_smallest()}")
    print(f"Smallest in {analyzer2.data}: {analyzer2.find_smallest()}")
    print(f"Smallest in {analyzer3.data}: {analyzer3.find_smallest()}")
    try:
        analyzer4 = ListAnalyzer([])
        print(analyzer4.find_smallest())
    except ValueError as e:
        print(e)