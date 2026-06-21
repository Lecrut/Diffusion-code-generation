class ItemFinder:
    def __init__(self, data):
        self.data = data

    def find_item(self, target):
        return target in self.data

if __name__ == '__main__':
    finder1 = ItemFinder([10, 25, 3, 42, 8, 15])
    result1 = finder1.find_item(42)
    print(f"List: {finder1.data}, Target: 42, Found: {result1}")
    
    finder2 = ItemFinder([1, 5, 9, 13, 17])
    result2 = finder2.find_item(100)
    print(f"List: {finder2.data}, Target: 100, Found: {result2}")
    
    finder3 = ItemFinder([5, 10, 15, 20])
    result3 = finder3.find_item(10)
    print(f"List: {finder3.data}, Target: 10, Found: {result3}")