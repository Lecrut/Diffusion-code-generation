class MinFinder:
    def get_smallest(self, data_list):
        if not data_list:
            raise ValueError("Input list cannot be empty")
        smallest = data_list[0]
        for item in data_list[1:]:
            if item < smallest:
                smallest = item
        return smallest
if __name__ == '__main__':
    finder = MinFinder()
    sample_data_1 = [5, 2, 8, 1, 9]
    sample_data_2 = [-10, 0, 50, -5]
    sample_data_3 = [42]
    sample_data_4 = []
    result_1 = finder.get_smallest(sample_data_1)
    print(f"Smallest in {sample_data_1}: {result_1}")
    result_2 = finder.get_smallest(sample_data_2)
    print(f"Smallest in {sample_data_2}: {result_2}")
    result_3 = finder.get_smallest(sample_data_3)
    print(f"Smallest in {sample_data_3}: {result_3}")
    try:
        finder.get_smallest(sample_data_4)
    except ValueError as e:
        print(f"Error for {sample_data_4}: {e}")