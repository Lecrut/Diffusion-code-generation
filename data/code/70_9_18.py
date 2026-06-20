class EndpointChecker:
    DEFAULT_VALUE = (None, None)

    @staticmethod
    def check_endpoints(iterable):
        if not iterable:
            return EndpointChecker.DEFAULT_VALUE
        first = next(iter(iterable))
        last = iterable[-1]
        return (first, last)

if __name__ == '__main__':
    checker = EndpointChecker()
    print(checker.check_endpoints([1, 2, 3, 4, 5]))
    print(checker.check_endpoints("hello"))
    print(checker.check_endpoints([]))
    print(checker.check_endpoints((10,)))