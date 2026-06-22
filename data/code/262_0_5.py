class MinMaxFinder:
    def __init__(self, data):
        self.data = data

    def find_min_max(self):
        if not self.data:
            return None, None
        min_val = max_val = self.data[0]
        for num in self.data[1:]:
            if num < min_val:
                min_val = num
            elif num > max_val:
                max_val = num
        return min_val, max_val

if __name__ == '__main__':
    finder = MinMaxFinder([42, 15, 89, 3, 77, 5])
    minimum, maximum = finder.find_min_max()
    print(f"Smallest element: {minimum}")
    print(f"Largest element: {maximum}")