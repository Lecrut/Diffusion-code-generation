class ListHandler:
    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError('Input must be a list')
        self.data = data

    def get_first_element(self):
        if len(self.data) == 0:
            return None
        return self.data[0]

if __name__ == '__main__':
    sample_list_1 = ListHandler([1, 2, 3])
    sample_list_2 = ListHandler([])
    sample_list_3 = ListHandler(['a', 'b', 'c'])
    
    print(sample_list_1.get_first_element())
    print(sample_list_2.get_first_element())
    print(sample_list_3.get_first_element())