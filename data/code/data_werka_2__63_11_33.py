def get_first_item(iterable):
    if not hasattr(iterable, '__iter__'):
        raise ValueError('The input is not an iterable')
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError('The iterable is empty')

class IterableHandler:
    def __init__(self, data):
        self.data = data
    def get_first(self):
        return get_first_item(self.data)

if __name__ == '__main__':
    sample_list = [7, 8, 9]
    sample_tuple = (10, 11, 12)
    sample_string = 'abc'
    
    handler_list = IterableHandler(sample_list)
    handler_tuple = IterableHandler(sample_tuple)
    handler_string = IterableHandler(sample_string)
    
    print(handler_list.get_first())
    print(handler_tuple.get_first())
    print(handler_string.get_first())