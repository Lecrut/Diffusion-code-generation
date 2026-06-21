class ListChecker:
    def get_extremes(self, data_list):
        if not data_list:
            return None
        first_element = data_list[0]
        last_element = data_list[-1]
        return (first_element, last_element)

if __name__ == '__main__':
    checker = ListChecker()
    sample_lists = {
        'numbers': [1, 5, 2, 8, 3],
        'letters': ['a', 'b', 'c', 'd'],
        'single_item': [42],
        'empty': []
    }
    
    for name, lst in sample_lists.items():
        result = checker.get_extremes(lst)
        print(f"Extremes of {name}: {result}")