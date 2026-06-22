class ElementFetcher:
    LIST_TYPE_ERROR = 'Input must be a list'
    
    @staticmethod
    def get_first_element(lst):
        if not isinstance(lst, list):
            raise ValueError(ElementFetcher.LIST_TYPE_ERROR)
        return lst[0] if lst else None

if __name__ == '__main__':
    sample_list = [4, 5, 6]
    empty_list = []
    non_list_input = 'not a list'
    
    try:
        print(ElementFetcher.get_first_element(sample_list))
    except ValueError as e:
        print(e)
    
    try:
        print(ElementFetcher.get_first_element(empty_list))
    except ValueError as e:
        print(e)
    
    try:
        print(ElementFetcher.get_first_element(non_list_input))
    except ValueError as e:
        print(e)