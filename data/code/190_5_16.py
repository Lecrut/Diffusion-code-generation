class ListInspector:
    @staticmethod
    def contains(data_list, item):
        return item in data_list

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    missing_item = 99
    empty_list = []
    result1 = ListInspector.contains(sample_list, 30)
    print(f"Does {sample_list} contain 30? {result1}")
    result2 = ListInspector.contains(empty_list, 5)
    print(f"Does {empty_list} contain 5? {result2}")