class ListChecker:
    def get_extremes(self, data_list):
        if not data_list:
            return None
        first_element = data_list[0]
        last_element = data_list[-1]
        return (first_element, last_element)

if __name__ == '__main__':
    checker = ListChecker()
    sample_list_one = [42, 3.14, 'apple', True]
    sample_list_two = ['banana', 'cherry']
    sample_list_empty = []
    
    result_one = checker.get_extremes(sample_list_one)
    result_two = checker.get_extremes(sample_list_two)
    result_empty = checker.get_extremes(sample_list_empty)
    
    print(f"Extremes of {sample_list_one}: {result_one}")
    print(f"Extremes of {sample_list_two}: {result_two}")
    print(f"Extremes of {sample_list_empty}: {result_empty}")