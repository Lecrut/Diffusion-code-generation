class MinFinder:
    def __init__(self, data=None):
        self.data = data if data is not None else []

    def find_minimum(self):
        if not self.data:
            raise ValueError("List cannot be empty")
        minimum = self.data[0]
        for item in self.data[1:]:
            if item < minimum:
                minimum = item
        return minimum

if __name__ == '__main__':
    min_finder1 = MinFinder([5, 2, 8, 1, 9])
    print(f"Minimum of [5, 2, 8, 1, 9]: {min_finder1.find_minimum()}")
    
    min_finder2 = MinFinder([-10, 0, 3, -5])
    print(f"Minimum of [-10, 0, 3, -5]: {min_finder2.find_minimum()}")
    
    min_finder3 = MinFinder([42])
    print(f"Minimum of [42]: {min_finder3.find_minimum()}")