class MiddleElementFinder:
    @staticmethod
    def find_middle(sequence):
        n = len(sequence)
        if n == 0:
            return None
        middle_index = n // 2
        return sequence[middle_index]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40, 50, 60],
        [1, 2, 3, 4],
        [100],
        []
    ]
    for i, lst in enumerate(sample_lists):
        result = MiddleElementFinder.find_middle(lst)
        print(f"Middle element of list {i+1}: {result}")