class MedianFinder:
    @staticmethod
    def find_middle_value(data):
        n = len(data)
        if n % 2 == 1:
            return data[n // 2]
        else:
            mid1 = data[n // 2 - 1]
            mid2 = data[n // 2]
            return (mid1 + mid2) / 2

if __name__ == '__main__':
    list1 = [1, 3, 2]
    list2 = [1, 5, 3, 4, 2]
    list3 = [10, 20, 30, 40]
    list4 = [7, 8, 9, 10]
    list5 = [1, 2, 3, 4, 5, 6]

    median_finder = MedianFinder()
    print(f"Median of {list1}: {median_finder.find_middle_value(list1)}")
    print(f"Median of {list2}: {median_finder.find_middle_value(list2)}")
    print(f"Median of {list3}: {median_finder.find_middle_value(list3)}")
    print(f"Median of {list4}: {median_finder.find_middle_value(list4)}")
    print(f"Median of {list5}: {median_finder.find_middle_value(list5)}")