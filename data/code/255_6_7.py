class MaxFinder:
    def __init__(self, data):
        self.data = data

    def find_max(self):
        max_val = self.data[0]
        for value in self.data:
            if value > max_val:
                max_val = value
        return max_val

if __name__ == '__main__':
    sample_data = [i for i in range(10**7)]
    finder = MaxFinder(sample_data)
    print(finder.find_max())