class ListAnalyzer:
    @staticmethod
    def get_median(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 1:
            median = sorted_data[n // 2]
        else:
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            median = (mid1 + mid2) / 2.0
        return median
if __name__ == '__main__':
    list1 = [1, 3, 5, 7, 9]
    list2 = [1, 2, 3, 4]
    list3 = [5, 2, 8, 1, 9]
    list4 = [10, 20, 30, 40, 50, 60]
    list5 = [7]
    list6 = []
    print(f"Median of {list1}: {ListAnalyzer.get_median(list1)}")
    print(f"Median of {list2}: {ListAnalyzer.get_median(list2)}")
    print(f"Median of {list3}: {ListAnalyzer.get_median(list3)}")
    print(f"Median of {list4}: {ListAnalyzer.get_median(list4)}")
    print(f"Median of {list5}: {ListAnalyzer.get_median(list5)}")
    try:
        ListAnalyzer.get_median(list6)
    except ValueError as e:
        print(f"Error for {list6}: {e}")