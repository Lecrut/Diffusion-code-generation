class LargestFinder:
    @staticmethod
    def find_largest(data):
        if not data:
            raise ValueError("Cannot find the largest element in an empty list.")
        largest = data[0]
        for item in data[1:]:
            if item > largest:
                largest = item
        return largest

if __name__ == '__main__':
    finder = LargestFinder()
    sample_list = [3, 5, 1, 8, 2]
    print(f"The largest element in {sample_list} is: {finder.find_largest(sample_list)}")