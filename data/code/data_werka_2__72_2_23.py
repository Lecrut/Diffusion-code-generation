class ListComparator:
    def compare_at_index(self, list1, list2, index):
        if not isinstance(index, int):
            raise ValueError("Index must be an integer")
        if index < 0 or index >= len(list1) or index >= len(list2):
            raise ValueError("Index out of range for one or both lists")
        
        first_item = list1[index]
        second_item = list2[index]
        
        if first_item < second_item:
            symbol = '<'
        elif first_item > second_item:
            symbol = '>'
        else:
            symbol = '='
            
        result = {
            'original_element1': first_item,
            'original_element2': second_item,
            'comparison_operator': symbol
        }
        return result

if __name__ == '__main__':
    comparator = ListComparator()
    sample_list_a = [10, 20, 30]
    sample_list_b = [10, 15, 30]
    target_index = 1
    
    output = comparator.compare_at_index(sample_list_a, sample_list_b, target_index)
    print(output)