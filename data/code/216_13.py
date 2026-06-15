class ListAnalyzer:
    def get_middle_value(self, data_list):
        n = len(data_list)
        if n == 0:
            return None
        else:
            middle_index = n // 2
            if n % 2 == 1:
                return data_list[middle_index]
            else:
                return (data_list[middle_index - 1] + data_list[middle_index]) / 2
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_list_odd = [1, 2, 3, 4, 5]
    sample_list_even = [10, 20, 30, 40]
    sample_list_single = [99]
    sample_list_empty = []
    print(f"Middle value of {sample_list_odd}: {analyzer.get_middle_value(sample_list_odd)}")
    print(f"Middle value of {sample_list_even}: {analyzer.get_middle_value(sample_list_even)}")
    print(f"Middle value of {sample_list_single}: {analyzer.get_middle_value(sample_list_single)}")
    print(f"Middle value of {sample_list_empty}: {analyzer.get_middle_value(sample_list_empty)}")