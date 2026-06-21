class ListChecker:
    def get_extremes(self, data_list):
        if not data_list:
            return None
        first_element = self.get_first(data_list)
        last_element = self.get_last(data_list)
        return (first_element, last_element)

    def get_first(self, data_list):
        return data_list[0]

    def get_last(self, data_list):
        return data_list[-1]

if __name__ == '__main__':
    checker = ListChecker()
    sample_list_one = [7, 3, 9, 2]
    sample_list_two = ['x', 'y', 'z']
    sample_list_empty = []
    result_one = checker.get_extremes(sample_list_one)
    result_two = checker.get_extremes(sample_list_two)
    result_empty = checker.get_extremes(sample_list_empty)
    print(f"Extremes of {sample_list_one}: {result_one}")
    print(f"Extremes of {sample_list_two}: {result_two}")
    print(f"Extremes of {sample_list_empty}: {result_empty}")