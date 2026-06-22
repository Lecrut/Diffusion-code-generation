class LargestFinder:
    def __init__(self, data):
        self.data = data
        self.largest = None

    def find_largest(self):
        if not self.data:
            raise ValueError("Input list cannot be empty")
        self.largest = self.data[0]
        for number in self.data[1:]:
            if number > self.largest:
                self.largest = number
        return self.largest

if __name__ == '__main__':
    finder1 = LargestFinder([1, 5, 2, 8, 3])
    finder2 = LargestFinder([-10, -5, -20, -1])
    finder3 = LargestFinder([42])
    empty_finder = LargestFinder([])
    
    print(f"Largest in {finder1.data}: {finder1.find_largest()}")
    print(f"Largest in {finder2.data}: {finder2.find_largest()}")
    print(f"Largest in {finder3.data}: {finder3.find_largest()}")
    try:
        finder4 = LargestFinder(empty_finder.data)
        print(f"Largest in empty list: {finder4.find_largest()}")
    except ValueError as e:
        print(e)