def get_first_element(lst):
    if not isinstance(lst, list):
        raise TypeError('Input must be a list')
    return lst[0] if lst else None

class ListProcessor:
    def __init__(self, data):
        self.data = data
    
    def first_element(self):
        return get_first_element(self.data)

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3]
    sample_list_2 = []
    sample_list_3 = ['a', 'b', 'c']
    
    processor_1 = ListProcessor(sample_list_1)
    processor_2 = ListProcessor(sample_list_2)
    processor_3 = ListProcessor(sample_list_3)
    
    print(processor_1.first_element())
    print(processor_2.first_element())
    print(processor_3.first_element())