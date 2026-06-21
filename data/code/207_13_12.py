from functools import reduce

class MaxFinder:
    def __init__(self, data):
        self.data = data
        self.current_max = reduce(lambda x, y: max(x, y), data)

    def get_current_max(self):
        return self.current_max

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6]
    finder = MaxFinder(sample_data)
    print("Current max:", finder.get_current_max())