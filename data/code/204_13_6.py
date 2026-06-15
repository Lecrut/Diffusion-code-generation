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
    list1 = [1, 3, 2]
    list2 = [5, 2, 8, 1, 9]
    list3 = [10, 20, 30, 40, 50]
    list4 = [7]
    list5 = []
    print(f"Median of {list1}: {ListAnalyzer.get_median(list1)}")
    print(f"Median of {list2}: {ListAnalyzer.get_median(list2)}")
    print(f"Median of {list3}: {ListAnalyzer.get_median(list3)}")
    print(f"Median of {list4}: {ListAnalyzer.get_median(list4)}")
    try:
        ListAnalyzer.get_median(list5)
    except ValueError as e:
        print(f"Error for {list5}: {e}")