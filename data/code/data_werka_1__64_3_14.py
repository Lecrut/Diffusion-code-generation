class ListHelper:
    @staticmethod
    def find_last_index(lst, value):
        return max((i for i, x in enumerate(lst) if x == value), default=-1)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target_value = 30
    last_index = ListHelper.find_last_index(sample_list, target_value)
    print(last_index)