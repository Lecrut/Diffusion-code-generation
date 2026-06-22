class MaxAdjacentPairs:
    @staticmethod
    def compare_adjacent(data):
        return [max(data[i:i+2]) for i in range(len(data) - 1)]

if __name__ == '__main__':
    sample_data = [1, 5, 2, 8, 8, 3, 0]
    max_pairs = MaxAdjacentPairs.compare_adjacent(sample_data)
    print(max_pairs)