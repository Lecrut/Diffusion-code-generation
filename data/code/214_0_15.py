class NumberFinder:
    def find_smallest(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        return min(data)

if __name__ == '__main__':
    sample_list = [42, 15, 89, 3, 77, 21]
    finder = NumberFinder()
    result = finder.find_smallest(sample_list)
    print(result)