class ListUtils:
    DEFAULT_VALUE = None

    @staticmethod
    def get_second_item(lst):
        try:
            return lst[1]
        except IndexError:
            return ListUtils.DEFAULT_VALUE

if __name__ == '__main__':
    sample_lists = [
        [10, 20, 30, 40, 50],
        [5],
        ['a', 'b', 'c'],
        []
    ]
    
    for idx, lst in enumerate(sample_lists):
        print(f"The second item in list {idx + 1} is: {ListUtils.get_second_item(lst)}")