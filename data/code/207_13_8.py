from functools import reduce

class MaxFinder:
    def __init__(self, data_stream):
        self.data_stream = data_stream
    
    def find_max(self):
        return reduce(lambda x, y: x if x > y else y, self.data_stream)

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6]
    finder = MaxFinder(sample_data)
    print("Maximum value:", finder.find_max())