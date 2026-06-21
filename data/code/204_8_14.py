class ArrayMiddleFinder:

    def find_middle(self, data):
        if not data:
            return None
        n = len(data)
        middle_index = n // 2
        return data[middle_index]
if __name__ == '__main__':
    finder = ArrayMiddleFinder()
    sample_data = [1, 2, 3, 4, 5]
    print(finder.find_middle(sample_data))
    empty_data = []
    print(finder.find_middle(empty_data))