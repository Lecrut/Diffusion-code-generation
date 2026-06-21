class ListMaxFinder:
    @staticmethod
    def find_max(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        max_val = data[0]
        for item in data[1:]:
            if item > max_val:
                max_val = item
        return max_val

if __name__ == '__main__':
    sample_values = [3, 5.5, 2, '10', -1]
    print(ListMaxFinder.find_max(sample_values))