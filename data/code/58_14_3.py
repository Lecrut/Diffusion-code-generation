class SafeListAccessor:
    def __init__(self, lst):
        self.lst = lst

    def get_first_element(self):
        try:
            return self.lst[0]
        except IndexError:
            return None

if __name__ == '__main__':
    sample_lists = [
        [10, 20, 30],
        [],
        ['hello', 'world'],
        [True, False, True]
    ]
    
    for i, lst in enumerate(sample_lists):
        accessor = SafeListAccessor(lst)
        print(f"First element of list {i+1}: {accessor.get_first_element()}")