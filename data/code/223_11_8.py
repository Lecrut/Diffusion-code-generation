class MaxFinder:
    def __init__(self, data):
        self.data = data

    def find_max(self):
        max_element = self.data[0]
        for number in self.data:
            if number > max_element:
                max_element = number
        return max_element

if __name__ == '__main__':
    sample_values = [3.14, 2.718, 1.618, 0.577, 1.414]
    finder = MaxFinder(sample_values)
    result = finder.find_max()
    print(result)