class ListHelper:
    @staticmethod
    def find_last_index(lst, value):
        return lst[::-1].index(value) if value in lst else -1

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    target_value = 50
    last_index = ListHelper.find_last_index(my_list, target_value)
    print(last_index)