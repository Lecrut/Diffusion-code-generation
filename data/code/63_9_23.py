class ListAnalyzer:

    def __init__(self, lst):
        self.lst = lst

    def find_first_value(self):
        if not self.lst:
            raise ValueError('The list is empty')
        return self.lst[0]
if __name__ == '__main__':
    sample_data = {'numbers': [1, 2, 3, 4], 'characters': ['a', 'b', 'c'], 'mixed': [True, False, 3.14], 'empty': []}
    for key, lst in sample_data.items():
        try:
            analyzer = ListAnalyzer(lst)
            print(f'First value of {key}: {analyzer.find_first_value()}')
        except ValueError as e:
            print(f'Error for {key}: {e}')