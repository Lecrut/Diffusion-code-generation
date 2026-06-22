class MinMaxFinder:
    def __init__(self, data):
        self.data = data

    def find_min(self):
        if not self.data:
            return None
        smallest = self.data[0]
        for element in self.data[1:]:
            if element < smallest:
                smallest = element
        return smallest

    def find_max(self):
        if not self.data:
            return None
        largest = self.data[0]
        for element in self.data[1:]:
            if element > largest:
                largest = element
        return largest

if __name__ == '__main__':
    sample_list = [34, 12, 56, 89, 3, 77, 21]
    finder = MinMaxFinder(sample_list)
    minimum = finder.find_min()
    maximum = finder.find_max()
    print(f"The list is: {sample_list}")
    print(f"The smallest element is: {minimum}")
    print(f"The largest element is: {maximum}")