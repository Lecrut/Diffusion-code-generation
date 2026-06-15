class ListAnalyzer:
    def get_middle_value(self, data_list):
        n = len(data_list)
        if n == 0:
            return None
        if n % 2 != 0:
            middle_index = n // 2
            return data_list[middle_index]
        else:
            middle_right_index = n // 2
            middle_left_index = middle_right_index - 1
            return (data_list[middle_left_index] + data_list[middle_right_index]) / 2
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40]
    list3 = [5, 15, 25, 35, 45]
    list4 = [1, 2, 3, 4]
    print(f"Middle value of {list1}: {analyzer.get_middle_value(list1)}")
    print(f"Middle value of {list2}: {analyzer.get_middle_value(list2)}")
    print(f"Middle value of {list3}: {analyzer.get_middle_value(list3)}")
    print(f"Middle value of {list4}: {analyzer.get_middle_value(list4)}")