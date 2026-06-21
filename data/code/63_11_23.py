def get_first_item(iterable):
    if not iterable:
        raise ValueError('The iterable is empty')
    return next(iter(iterable))

class IterableProcessor:
    def __init__(self, data):
        self.data = data

    def first_item(self):
        return get_first_item(self.data)

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = (40, 50, 60)
    sample_string = 'world'
    
    processor_list = IterableProcessor(sample_list)
    processor_tuple = IterableProcessor(sample_tuple)
    processor_string = IterableProcessor(sample_string)

    print(processor_list.first_item())
    print(processor_tuple.first_item())
    print(processor_string.first_item())