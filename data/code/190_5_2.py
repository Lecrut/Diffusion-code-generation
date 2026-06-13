class ListContainer:
    @staticmethod
    def contains(data_list, item):
        return item in data_list
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    item_to_find_present = 30
    item_to_find_absent = 99
    empty_list = []
    result1 = ListContainer.contains(sample_list, item_to_find_present)
    print(f"Does {sample_list} contain {item_to_find_present}? {result1}")
    result2 = ListContainer.contains(sample_list, item_to_find_absent)
    print(f"Does {sample_list} contain {item_to_find_absent}? {result2}")
    result3 = ListContainer.contains(empty_list, 5)
    print(f"Does {empty_list} contain 5? {result3}")