class MinFinder:
    def __init__(self, data):
        self.data = data
    
    def find_min(self):
        if not self.data:
            raise ValueError("List cannot be empty")
        min_val = self.data[0]
        for num in self.data[1:]:
            if num < min_val:
                min_val = num
        return min_val

if __name__ == '__main__':
    finder1 = MinFinder([5, 2, 8, 1, 9])
    print(f"Minimum of [5, 2, 8, 1, 9]: {finder1.find_min()}")
    
    finder2 = MinFinder([-10, 0, -5, 3])
    print(f"Minimum of [-10, 0, -5, 3]: {finder2.find_min()}")