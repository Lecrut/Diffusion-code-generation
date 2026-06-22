class EndpointChecker:
    DEFAULT_EMPTY_VALUE = None

    @staticmethod
    def _validate_iterable(obj):
        try:
            iter(obj)
        except TypeError:
            raise ValueError("Input must be an iterable")
        return obj

    @staticmethod
    def _get_first(iterator):
        return next(iterator)

    def check_endpoints(self, iterable):
        validated = self._validate_iterable(iterable)
        iterator = iter(validated)
        try:
            first = self._get_first(iterator)
        except StopIteration:
            return self.DEFAULT_EMPTY_VALUE, self.DEFAULT_EMPTY_VALUE
        
        last = first
        for item in iterator:
            last = item
        
        return first, last

if __name__ == '__main__':
    checker = EndpointChecker()
    
    sample_list = [10, 20, 30, 40, 50]
    first, last = checker.check_endpoints(sample_list)
    print(f"List: first={first}, last={last}")
    
    sample_string = "Python"
    first, last = checker.check_endpoints(sample_string)
    print(f"String: first={first}, last={last}")
    
    empty_list = []
    first, last = checker.check_endpoints(empty_list)
    print(f"Empty: first={first}, last={last}")
    
    single_item = [99]
    first, last = checker.check_endpoints(single_item)
    print(f"Single: first={first}, last={last}")