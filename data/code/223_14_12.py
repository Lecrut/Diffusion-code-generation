class MaxFinder:
    def find_max(self, data):
        if not data:
            raise ValueError("List cannot be empty")
        max_val = data[0]
        for item in data[1:]:
            if item > max_val:
                max_val = item
        return max_val

if __name__ == '__main__':
    finder = MaxFinder()
    sample_data = [3, 5, 1, 2, 4]
    print(finder.find_max(sample_data))