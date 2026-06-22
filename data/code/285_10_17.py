class MaxAdjacent:
    def __init__(self, data):
        self.data = data

    def compare_adjacent(self):
        return [max(self.data[i:i+2]) for i in range(len(self.data) - 1)]

if __name__ == '__main__':
    sample_data = [1, 5, 2, 8, 8, 3, 0]
    max_finder = MaxAdjacent(sample_data)
    print(max_finder.compare_adjacent())