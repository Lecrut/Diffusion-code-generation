class MinFinder:
    def __init__(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        self.minimum = data[0]

    def get_minimum(self):
        return self.minimum

if __name__ == '__main__':
    finder1 = MinFinder([5, 2, 8, 1, 9])
    print(f"Minimum of {finder1.get_minimum()}: {finder1.get_minimum()}")
    
    finder3 = MinFinder([-10, -5, -20])
    print(f"Minimum of {finder3.get_minimum()}: {finder3.get_minimum()}")
    
    try:
        finder2 = MinFinder([])
    except ValueError as e:
        print(e)