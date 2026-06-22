class ListFinder:
    @staticmethod
    def find_last_index(lst, value):
        last_index = -1
        for i in range(len(lst)):
            if lst[i] == value:
                last_index = i
        return last_index

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 2, 5, 2]
    value_to_find = 2
    finder = ListFinder()
    index = finder.find_last_index(sample_list, value_to_find)
    print(index)