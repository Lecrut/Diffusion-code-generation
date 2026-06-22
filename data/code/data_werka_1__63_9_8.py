class ListHandler:
    @staticmethod
    def get_first_element(data_list):
        if not data_list:
            raise ValueError("The input list is empty")
        return data_list[0]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    result = ListHandler.get_first_element(sample_data)
    print(result)
    
    try:
        sample_data_empty = []
        result_empty = ListHandler.get_first_element(sample_data_empty)
        print(result_empty)
    except ValueError as e:
        print(e)
    
    sample_data_single = [99]
    result_single = ListHandler.get_first_element(sample_data_single)
    print(result_single)