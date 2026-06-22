class EndpointChecker:
    EMPTY_RESULT = (None, None)

    @staticmethod
    def _validate_iterable(obj):
        try:
            iter(obj)
        except TypeError:
            raise ValueError("Input must be an iterable")
        return obj

    @staticmethod
    def check_endpoints(iterable):
        iterable = EndpointChecker._validate_iterable(iterable)
        iterator = iter(iterable)
        try:
            first = next(iterator)
        except StopIteration:
            return EndpointChecker.EMPTY_RESULT
        
        last = first
        for item in iterator:
            last = item
            
        return first, last

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(EndpointChecker.check_endpoints(sample_data))
    
    empty_data = []
    print(EndpointChecker.check_endpoints(empty_data))
    
    string_data = "python"
    print(EndpointChecker.check_endpoints(string_data))
    
    single_data = [99]
    print(EndpointChecker.check_endpoints(single_data))