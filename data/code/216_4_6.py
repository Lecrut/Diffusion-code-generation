class ListAnalyzer:
    def find_middle(self, data):
        n = len(data)
        if n == 0:
            return None
        if n % 2 != 0:
            middle_index = n // 2
            return data[middle_index]
        else:
            middle_right_index = n // 2
            middle_left_index = middle_right_index - 1
            return (data[middle_left_index] + data[middle_right_index]) // 2
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40]
    list3 = [5, 9, 12, 15, 18]
    list4 = [1, 2, 3, 4]
    print(f"Middle of {list1}: {analyzer.find_middle(list1)}")
    print(f"Middle of {list2}: {analyzer.find_middle(list2)}")
    print(f"Middle of {list3}: {analyzer.find_middle(list3)}")
    print(f"Middle of {list4}: {analyzer.find_middle(list4)}")