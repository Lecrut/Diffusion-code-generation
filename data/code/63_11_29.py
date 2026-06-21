class IterableUtils:
    @staticmethod
    def get_first_item(iterable):
        if not iterable:
            raise ValueError('The iterable is empty')
        return next(iter(iterable))

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_tuple = (4, 5, 6)
    sample_string = 'abc'
    sample_set = {7, 8, 9}
    
    print(IterableUtils.get_first_item(sample_list))
    print(IterableUtils.get_first_item(sample_tuple))
    print(IterableUtils.get_first_item(sample_string))
    print(IterableUtils.get_first_item(sample_set))