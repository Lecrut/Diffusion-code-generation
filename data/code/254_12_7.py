class MinFinder:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def find_min(self):
        if not self.numbers:
            raise ValueError("List cannot be empty")
        min_val = self.numbers[0]
        for num in self.numbers[1:]:
            if num < min_val:
                min_val = num
        return min_val

if __name__ == '__main__':
    finder1 = MinFinder([5, 2, 8, 1, 9])
    print(f"Minimum of [5, 2, 8, 1, 9]: {finder1.find_min()}")
    finder2 = MinFinder([-10, 0, -5, 3])
    print(f"Minimum of [-10, 0, -5, 3]: {finder2.find_min()}")