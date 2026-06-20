class ListChecker:
    def get_extremes(self, data_list):
        if not data_list:
            return None
        extremes = {'first': data_list[0], 'last': data_list[-1]}
        return extremes

if __name__ == '__main__':
    checker = ListChecker()
    sample_list_one = [1, 5, 2, 8, 3]
    sample_list_two = ['a', 'b', 'c', 'd']
    result_one = checker.get_extremes(sample_list_one)
    result_two = checker.get_extremes(sample_list_two)
    print(f"Extremes of {sample_list_one}: {result_one}")
    print(f"Extremes of {sample_list_two}: {result_two}")