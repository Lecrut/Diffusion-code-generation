class ListChecker:
    def get_extremes(self, data_list):
        if not data_list:
            return None
        first_element = data_list[0]
        last_element = data_list[-1]
        return (first_element, last_element)

if __name__ == '__main__':
    checker = ListChecker()
    sample_list_one = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sample_list_two = ['apple', 'banana', 'cherry']
    sample_list_three = []
    
    result_one = checker.get_extremes(sample_list_one)
    result_two = checker.get_extremes(sample_list_two)
    result_three = checker.get_extremes(sample_list_three)

    print(f"Extremes of {sample_list_one}: {result_one}")
    print(f"Extremes of {sample_list_two}: {result_two}")
    print(f"Extremes of {sample_list_three}: {result_three}")