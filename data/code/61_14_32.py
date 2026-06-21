class ListElementRetriever:
    @staticmethod
    def get_element_at_index(lst, index):
        if not isinstance(lst, list):
            raise TypeError('The first argument must be a list.')
        if not isinstance(index, int):
            raise TypeError('The index must be an integer.')
        
        length = len(lst)
        if index < 0:
            index += length
        if index < 0 or index >= length:
            raise IndexError('Index out of range.')
        
        return lst[index]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    try:
        print(ListElementRetriever.get_element_at_index(sample_list, 1))
        print(ListElementRetriever.get_element_at_index(sample_list, -2))
        print(ListElementRetriever.get_element_at_index(sample_list, 6))
    except (TypeError, IndexError) as e:
        print(e)