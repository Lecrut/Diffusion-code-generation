class ListAnalyzer:
    DEFAULT_THRESHOLD = 0

    @staticmethod
    def find_last_greater_equal(data, threshold=DEFAULT_THRESHOLD):
        n = len(data)
        result = -1
        for i in range(n - 1, -1, -1):
            if data[i] >= threshold:
                result = i
                break
        return result

if __name__ == '__main__':
    list1 = [10, 5, 20, 15, 30, 25]
    threshold1 = 20
    print(ListAnalyzer.find_last_greater_equal(list1, threshold1))

    list2 = [3, 1, 4, 1, 5, 9, 2, 6]
    threshold2 = 5
    print(ListAnalyzer.find_last_greater_equal(list2, threshold2))

    list3 = [1, 2, 3, 4, 5]
    threshold3 = 6
    print(ListAnalyzer.find_last_greater_equal(list3, threshold3))