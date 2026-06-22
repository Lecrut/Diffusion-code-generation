def get_first_element(lst):
    if not lst:
        raise ValueError("The input list is empty")
    return lst[0]

class ListHandler:
    @staticmethod
    def fetch_first_element(lst):
        return get_first_element(lst)

if __name__ == '__main__':
    sample_list = [15, 25, 35, 45, 55]
    try:
        print(ListHandler.fetch_first_element(sample_list))
    except ValueError as e:
        print(e)
    
    empty_list = []
    try:
        print(ListHandler.fetch_first_element(empty_list))
    except ValueError as e:
        print(e)
    
    single_element_list = [100]
    try:
        print(ListHandler.fetch_first_element(single_element_list))
    except ValueError as e:
        print(e)