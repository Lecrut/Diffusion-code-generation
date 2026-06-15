class ListAnalyzer:
    def get_max(self, data_list):
        if not data_list:
            raise ValueError("Input list cannot be empty")
        max_value = data_list[0]
        for item in data_list:
            if item > max_value:
                max_value = item
        return max_value
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_list1 = [1, 5, 2, 8, 3]
    sample_list2 = [-10, -5, -20, -1]
    sample_list3 = [42]
    sample_list4 = []
    print(f"Max of {sample_list1}: {analyzer.get_max(sample_list1)}")
    print(f"Max of {sample_list2}: {analyzer.get_max(sample_list2)}")
    print(f"Max of {sample_list3}: {analyzer.get_max(sample_list3)}")
    try:
        analyzer.get_max(sample_list4)
    except ValueError as e:
        print(f"Error for {sample_list4}: {e}")