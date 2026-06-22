class ListComparator:
    def __init__(self):
        self._valid_operators = ('<', '>', '=')

    def _validate_lists(self, list1, list2, index):
        if not isinstance(list1, (list, tuple)):
            raise ValueError("list1 must be a list or tuple")
        if not isinstance(list2, (list, tuple)):
            raise ValueError("list2 must be a list or tuple")
        if not isinstance(index, int):
            raise ValueError("index must be an integer")
        if index < 0:
            raise ValueError("index must be non-negative")
        if index >= len(list1):
            raise ValueError("index out of range for list1")
        if index >= len(list2):
            raise ValueError("index out of range for list2")

    def compare_at_index(self, list1, list2, index):
        self._validate_lists(list1, list2, index)
        item_a = list1[index]
        item_b = list2[index]
        
        if item_a < item_b:
            symbol = '<'
        elif item_a > item_b:
            symbol = '>'
        else:
            symbol = '='
            
        return {
            'left_element': item_a,
            'right_element': item_b,
            'comparison_result': symbol
        }

if __name__ == '__main__':
    comparator = ListComparator()
    data_a = [10, 20, 30]
    data_b = [15, 10, 30]
    result = comparator.compare_at_index(data_a, data_b, 0)
    print(result)
    result2 = comparator.compare_at_index(data_a, data_b, 1)
    print(result2)
    result3 = comparator.compare_at_index(data_a, data_b, 2)
    print(result3)