class ListAnalyzer:
    @staticmethod
    def get_median(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 1:
            middle_index = n // 2
            return sorted_data[middle_index]
        else:
            middle_right_index = n // 2
            middle_left_index = middle_right_index - 1
            median = (sorted_data[middle_left_index] + sorted_data[middle_right_index]) / 2
            return median
if __name__ == '__main__':
    list1 = [1, 3, 5, 7, 9]
    list2 = [1, 2, 3, 4, 5, 6]
    list3 = [10, 40, 20, 30]
    list4 = [7, 2, 9, 4, 1]
    list5 = [5]
    print(f"Median of {list1}: {ListAnalyzer.get_median(list1)}")
    print(f"Median of {list2}: {ListAnalyzer.get_median(list2)}")
    print(f"Median of {list3}: {ListAnalyzer.get_median(list3)}")
    print(f"Median of {list4}: {ListAnalyzer.get_median(list4)}")
    print(f"Median of {list5}: {ListAnalyzer.get_median(list5)}")