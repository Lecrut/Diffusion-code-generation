class ListChecker:
    def get_extremes(self, data_list):
        if not data_list:
            return None
        first = data_list[0]
        last = data_list[-1]
        return (first, last)
if __name__ == '__main__':
    checker = ListChecker()
    sample_list_1 = [1, 5, 2, 8, 3]
    sample_list_2 = ['a', 'b', 'c', 'd']
    sample_list_3 = [100]
    sample_list_4 = []
    result_1 = checker.get_extremes(sample_list_1)
    result_2 = checker.get_extremes(sample_list_2)
    result_3 = checker.get_extremes(sample_list_3)
    result_4 = checker.get_extremes(sample_list_4)
    print(f"List 1 extremes: {result_1}")
    print(f"List 2 extremes: {result_2}")
    print(f"List 3 extremes: {result_3}")
    print(f"List 4 extremes: {result_4}")