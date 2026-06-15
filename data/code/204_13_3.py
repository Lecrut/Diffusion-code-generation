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
            mid1_index = n // 2 - 1
            mid2_index = n // 2
            median = (sorted_data[mid1_index] + sorted_data[mid2_index]) / 2
            return median
if __name__ == '__main__':
    list1 = [1, 3, 2]
    list2 = [5, 2, 8, 1, 9]
    list3 = [10, 4, 7, 2, 1]
    list4 = [1, 2, 3, 4, 5]
    list5 = [1, 2, 3, 4]
    print(f"Median of {list1}: {ListAnalyzer.get_median(list1)}")
    print(f"Median of {list2}: {ListAnalyzer.get_median(list2)}")
    print(f"Median of {list3}: {ListAnalyzer.get_median(list3)}")
    print(f"Median of {list4}: {ListAnalyzer.get_median(list4)}")
    print(f"Median of {list5}: {ListAnalyzer.get_median(list5)}")