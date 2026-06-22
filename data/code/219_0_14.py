class MaxFinder:
    def find_max(self, numbers):
        if not numbers:
            raise ValueError("Input list cannot be empty")
        return max(numbers)

if __name__ == '__main__':
    finder = MaxFinder()
    sample_list1 = [1, 5, 2, 8, 3]
    sample_list2 = [-10, -5, -20, -1]
    sample_list3 = [42]
    sample_list4 = []
    
    print(f"Max of {sample_list1}: {finder.find_max(sample_list1)}")
    print(f"Max of {sample_list2}: {finder.find_max(sample_list2)}")
    print(f"Max of {sample_list3}: {finder.find_max(sample_list3)}")
    try:
        finder.find_max(sample_list4)
    except ValueError as e:
        print(e)