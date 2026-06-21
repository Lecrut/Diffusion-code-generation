class ListAnalyzer:
    def __init__(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        self.data = data

    def find_largest(self):
        return max(self.data)

if __name__ == '__main__':
    analyzer1 = ListAnalyzer([10, 5, 22, 8, 30])
    print(f"List: {analyzer1.data}, Largest: {analyzer1.find_largest()}")

    analyzer2 = ListAnalyzer([-5, -1, -10, -2])
    print(f"List: {analyzer2.data}, Largest: {analyzer2.find_largest()}")

    analyzer3 = ListAnalyzer([42])
    print(f"List: {analyzer3.data}, Largest: {analyzer3.find_largest()}")