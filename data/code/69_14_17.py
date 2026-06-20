class ListAccessor:
    @staticmethod
    def get_first_last_middle_elements(input_list):
        if not input_list:
            return ()
        
        first_element = input_list[0]
        last_element = input_list[-1]
        middle_index = len(input_list) // 2
        middle_element = input_list[middle_index]
        
        return (first_element, last_element, middle_element)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = ListAccessor.get_first_last_middle_elements(sample_list)
    print(result)