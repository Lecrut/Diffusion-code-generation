class MiddleFinder:
    DEFAULT_LIST = [1, 2, 3, 4, 5]

    @staticmethod
    def find_middle(sequence):
        n = len(sequence)
        if n == 0:
            return None
        middle_index = n // 2
        return sequence[middle_index]

if __name__ == '__main__':
    sample_lists = {
        'odd': [1, 3, 5, 7, 9],
        'even': [2, 4, 6, 8, 10, 12],
        'single': [42],
        'empty': [],
        'default': MiddleFinder.DEFAULT_LIST
    }
    for key, lst in sample_lists.items():
        result = MiddleFinder.find_middle(lst)
        print(f"Middle element of {key} list: {result}")