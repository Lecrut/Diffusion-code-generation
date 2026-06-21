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
    
    print(f"Smallest in {sample_data_1}: {finder.get_smallest(sample_data_1)}")
    print(f"Smallest in {sample_data_2}: {finder.get_smallest(sample_data_2)}")
    print(f"Smallest in {sample_data_3}: {finder.get_smallest(sample_data_3)}")