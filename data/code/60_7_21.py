class ListUtilities:
    @staticmethod
    def get_last_element(lst):
        if not lst:
            raise IndexError("Cannot retrieve the last element from an empty list.")
        return lst[-1]

if __name__ == '__main__':
    sample_lists = {
        'fruits': ['apple', 'banana', 'cherry'],
        'numbers': [10, 20, 30, 40],
        'empty': [],
    }
    
    for name, lst in sample_lists.items():
        try:
            result = ListUtilities.get_last_element(lst)
            print(f"Last element of {name}: {result}")
        except IndexError as e:
            print(f"Error accessing last element of {name}: {e}")