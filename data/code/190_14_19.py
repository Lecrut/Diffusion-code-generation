class ListSearch:
    @staticmethod
    def contains_item(lst, value):
        return value in set(lst)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    search_value = 3
    print(ListSearch.contains_item(sample_list, search_value))