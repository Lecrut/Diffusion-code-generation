class MinFinder:
    def find_minimum(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        return min(data)

if __name__ == '__main__':
    finder = MinFinder()
    sample_list = [45, 12, 89, 3, 56, 7]
    minimum_value = finder.find_minimum(sample_list)
    print(minimum_value)