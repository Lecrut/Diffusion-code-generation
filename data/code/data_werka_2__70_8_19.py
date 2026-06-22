class EndpointChecker:
    def __init__(self, data):
        self.data = data

    def get_endpoints(self):
        iterator = iter(self.data)
        try:
            first = next(iterator)
        except StopIteration:
            return None, None
        last = first
        for item in iterator:
            last = item
        return first, last

def check_endpoints(iterable):
    checker = EndpointChecker(iterable)
    return checker.get_endpoints()

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = check_endpoints(sample_list)
    print(result)
    
    empty_list = []
    empty_result = check_endpoints(empty_list)
    print(empty_result)
    
    sample_string = "python"
    string_result = check_endpoints(sample_string)
    print(string_result)
    
    single_item = [42]
    single_result = check_endpoints(single_item)
    print(single_result)