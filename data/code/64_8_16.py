class IndexFinder:
    @staticmethod
    def find_last_greater_equal(data, threshold):
        n = len(data)
        result = -1
        for i in range(n - 1, -1, -1):
            if data[i] >= threshold:
                result = i
                break
        return result

if __name__ == '__main__':
    list1 = [50, 40, 30, 20, 10]
    threshold1 = 25
    print(IndexFinder.find_last_greater_equal(list1, threshold1))
    
    list2 = [1, 2, 3, 4, 5, 6]
    threshold2 = 7
    print(IndexFinder.find_last_greater_equal(list2, threshold2))
    
    list3 = [100, 200, 300, 400, 500]
    threshold3 = 350
    print(IndexFinder.find_last_greater_equal(list3, threshold3))