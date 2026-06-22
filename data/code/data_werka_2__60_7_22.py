class ListUtility:
    @staticmethod
    def get_last_element(lst):
        if not isinstance(lst, list):
            raise TypeError("Input must be a list.")
        if not lst:
            raise IndexError("Cannot retrieve the last element from an empty list.")
        return lst[-1]

if __name__ == '__main__':
    sample_lists = {
        'list1': [10, 20, 30, 40, 50],
        'empty_list': [],
        'list_with_strings': ['a', 'b', 'c']
    }
    
    for name, lst in sample_lists.items():
        try:
            result = ListUtility.get_last_element(lst)
            print(f"Last element of {name}: {result}")
        except (IndexError, TypeError) as e:
            print(f"Error accessing last element of {name}: {e}")