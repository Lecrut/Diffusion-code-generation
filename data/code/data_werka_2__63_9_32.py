class ListAnalyzer:
    def __init__(self, lst):
        self.lst = lst

    def is_list_empty(self):
        return len(self.lst) == 0

    def find_first_value(self):
        if self.is_list_empty():
            raise ValueError("The list is empty")
        return self.lst[0]

if __name__ == '__main__':
    sample_lists = [
        [42, 84, 168],
        ['hello', 'world'],
        [],
        [True, False, None]
    ]
    
    for i, lst in enumerate(sample_lists):
        try:
            analyzer = ListAnalyzer(lst)
            print(f"First value of list {i+1}: {analyzer.find_first_value()}")
        except ValueError as e:
            print(f"Error for list {i+1}: {e}")