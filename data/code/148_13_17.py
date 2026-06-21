class MaxElementFinder:
    @staticmethod
    def find_largest_element(data):
        if not data:
            raise ValueError("The list cannot be empty")
        largest = max(data)
        return largest

if __name__ == '__main__':
    sample_list = [15, 8, 42, 3, 99, 21]
    largest = MaxElementFinder.find_largest_element(sample_list)
    print(largest)