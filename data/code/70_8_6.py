class EndpointChecker:
    EMPTY_RESULT = (None, None)

    @staticmethod
    def _get_first(it):
        return next(it)

    @staticmethod
    def _get_last(it, first):
        last = first
        for item in it:
            last = item
        return last

    def check_endpoints(self, iterable):
        try:
            it = iter(iterable)
            first = self._get_first(it)
            last = self._get_last(it, first)
            return first, last
        except StopIteration:
            return self.EMPTY_RESULT
        except TypeError:
            raise ValueError("Input must be an iterable")

if __name__ == '__main__':
    checker = EndpointChecker()
    result = checker.check_endpoints([10, 20, 30, 40])
    print(result)
    empty_result = checker.check_endpoints([])
    print(empty_result)
    string_result = checker.check_endpoints("python")
    print(string_result)