class Finder:
    def __init__(self, data_list):
        self.data_list = data_list

    def find_final_index(self, target_item):
        last_index = -1
        for index, item in enumerate(self.data_list):
            if item == target_item:
                last_index = index
        return last_index

if __name__ == '__main__':
    list1 = [1, 2, 3, 2, 4, 2, 5]
    finder1 = Finder(list1)
    result1 = finder1.find_final_index(2)
    print(f"List: {list1}, Target: 2, Final Index: {result1}")

    list2 = ['a', 'b', 'c', 'b', 'd', 'b']
    finder2 = Finder(list2)
    result2 = finder2.find_final_index('b')
    print(f"List: {list2}, Target: 'b', Final Index: {result2}")

    list3 = [10, 20, 30, 40]
    finder3 = Finder(list3)
    result3 = finder3.find_final_index(5)
    print(f"List: {list3}, Target: 5, Final Index: {result3}")