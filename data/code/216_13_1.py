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
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [10, 20, 30, 40]
    sample_list3 = [5, 8, 12, 15]
    sample_list4 = [7]
    sample_list5 = []
    print(f"Middle value of {sample_list1}: {analyzer.get_middle_value(sample_list1)}")
    print(f"Middle value of {sample_list2}: {analyzer.get_middle_value(sample_list2)}")
    print(f"Middle value of {sample_list3}: {analyzer.get_middle_value(sample_list3)}")
    print(f"Middle value of {sample_list4}: {analyzer.get_middle_value(sample_list4)}")
    print(f"Middle value of {sample_list5}: {analyzer.get_middle_value(sample_list5)}")