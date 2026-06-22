class EndpointExtractor:
    _EMPTY_RESULT = []
    _SINGLE_RESULT = None

    @staticmethod
    def _validate_iterable(obj):
        if obj is None:
            raise ValueError("Input cannot be None")
        return iter(obj)

    @staticmethod
    def _extract_endpoints(iterator):
        try:
            first = next(iterator)
        except StopIteration:
            return EndpointExtractor._EMPTY_RESULT
        
        last = first
        has_more = False
        
        for item in iterator:
            last = item
            has_more = True
        
        if has_more:
            return [first, last]
        return [first]

    def get_endpoints(self, iterable):
        iterator = self._validate_iterable(iterable)
        return self._extract_endpoints(iterator)

if __name__ == '__main__':
    extractor = EndpointExtractor()
    
    sample_list = [10, 20, 30, 40, 50]
    result_list = extractor.get_endpoints(sample_list)
    print(result_list)
    
    sample_single = [42]
    result_single = extractor.get_endpoints(sample_single)
    print(result_single)
    
    sample_empty = []
    result_empty = extractor.get_endpoints(sample_empty)
    print(result_empty)
    
    sample_string = "Python"
    result_string = extractor.get_endpoints(sample_string)
    print(result_string)