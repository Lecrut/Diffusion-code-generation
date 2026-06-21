class LargestNumberFinder:
    @staticmethod
    def find_largest(data):
        if not data:
            return None
        largest = data[0]
        for element in data[1:]:
            if element > largest:
                largest = element
        return largest

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Largest number in sample list:", LargestNumberFinder.find_largest(sample_list))
    large_sample = [100, 50, 200, 10, 300, 150]
    print("Largest number in large sample list:", LargestNumberFinder.find_largest(large_sample))