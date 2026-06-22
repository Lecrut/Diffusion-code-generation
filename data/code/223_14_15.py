class ListMaxFinder:
    def find_max_iterative(self, data):
        if not data:
            raise ValueError("List cannot be empty")
        max_val = data[0]
        for item in data[1:]:
            if item > max_val:
                max_val = item
        return max_val

if __name__ == '__main__':
    finder = ListMaxFinder()
    sample_data = [3, 5, 1, 8, 2, 9, 4]
    print("Maximum value using iterative method:", finder.find_max_iterative(sample_data))