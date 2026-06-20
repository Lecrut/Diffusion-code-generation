class MedianFinder:
    @staticmethod
    def find_median(data):
        n = len(data)
        if n == 0:
            return None
        sorted_data = sorted(data)
        middle_index = n // 2
        return sorted_data[middle_index] if n % 2 == 1 else sorted_data[middle_index - 1]

if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = [10, 20, 30, 40]
    list3 = [7, 1, 5, 2, 8, 3, 9]
    list4 = [1, 2, 3, 4, 5, 6]
    list5 = [100]

    print(MedianFinder.find_median(list1))
    print(MedianFinder.find_median(list2))
    print(MedianFinder.find_median(list3))
    print(MedianFinder.find_median(list4))
    print(MedianFinder.find_median(list5))