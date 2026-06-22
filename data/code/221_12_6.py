class SortedNumbers:
    def __init__(self, x, y, z):
        self.values = [x, y, z]
    
    def sort_values(self):
        return sorted(self.values)

if __name__ == '__main__':
    numbers = SortedNumbers(7, 1, 4)
    print(numbers.sort_values())