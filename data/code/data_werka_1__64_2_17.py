class ListFinder:
    @staticmethod
    def find_last_index(lst, value):
        last_index = -1
        for index in range(len(lst)):
            if lst[index] == value:
                last_index = index
        return last_index

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 2, 5, 2]
    value_to_find = 2
    result = ListFinder.find_last_index(sample_list, value_to_find)
    print(result)