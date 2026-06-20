class ListUtils:

    @staticmethod
    def find_middle(data):
        n = len(data)
        if n == 0:
            return None
        middle_index = n // 2
        return data[middle_index]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30]
    list3 = [50]
    list4 = []
    list5 = [1, 2, 3, 4]
    list6 = [100, 200]
    print(ListUtils.find_middle(list1))
    print(ListUtils.find_middle(list2))
    print(ListUtils.find_middle(list3))
    print(ListUtils.find_middle(list4))
    print(ListUtils.find_middle(list5))
    print(ListUtils.find_middle(list6))