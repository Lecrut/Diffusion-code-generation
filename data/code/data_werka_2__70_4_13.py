class EndpointExtractor:
    _EMPTY_RESULT = []
    _SINGLE_RESULT = None

    @staticmethod
    def _validate_iterable(iterable):
        if iterable is None:
            raise ValueError("Input cannot be None")
        return iter(iterable)

    @staticmethod
    def _extract_first(iterator):
        try:
            return next(iterator)
        except StopIteration:
            return None

    @classmethod
    def get_endpoints(cls, iterable):
        iterator = cls._validate_iterable(iterable)
        first = cls._extract_first(iterator)
        if first is None:
            return cls._EMPTY_RESULT
        
        last = first
        for item in iterator:
            last = item
        
        if first == last:
            return [first]
        return [first, last]

    @classmethod
    def get_endpoints_generator(cls, iterable):
        iterator = cls._validate_iterable(iterable)
        first = cls._extract_first(iterator)
        if first is None:
            return
        last = first
        for item in iterator:
            last = item
        yield first
        if first != last:
            yield last

if __name__ == '__main__':
    data_list = [1, 2, 3, 4, 5]
    extractor = EndpointExtractor()
    result_list = extractor.get_endpoints(data_list)
    print(result_list)
    
    result_gen = list(extractor.get_endpoints_generator(data_list))
    print(result_gen)
    
    single_item = [42]
    print(extractor.get_endpoints(single_item))
    
    empty_item = []
    print(extractor.get_endpoints(empty_item))