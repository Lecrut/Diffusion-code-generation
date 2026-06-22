class MaxFinder:
    def __init__(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        self.data = data

    def find_max(self):
        return max(self.data)

if __name__ == '__main__':
    finder1 = MaxFinder([3, 1, 4, 1, 5, 9, 2])
    finder2 = MaxFinder([-10, -5, -20, -1])
    finder3 = MaxFinder([7])
    try:
        finder4 = MaxFinder([])
    except ValueError as e:
        print(e)

    print(f"Max of {finder1.data}: {finder1.find_max()}")
    print(f"Max of {finder2.data}: {finder2.find_max()}")
    print(f"Max of {finder3.data}: {finder3.find_max()}")