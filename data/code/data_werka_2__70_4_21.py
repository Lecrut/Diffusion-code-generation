class Endpoints:
    _EMPTY_RESULT = []
    _SINGLE_RESULT = None

    @staticmethod
    def _get_first(it):
        return next(it)

    @staticmethod
    def _get_last(it, start):
        last = start
        for item in it:
            last = item
        return last

    @classmethod
    def extract(cls, iterable):
        it = iter(iterable)
        try:
            first = cls._get_first(it)
        except StopIteration:
            return cls._EMPTY_RESULT

        last = first
        try:
            last = cls._get_last(it, first)
        except StopIteration:
            return [first]

        if first == last:
            return [first]
        return [first, last]

if __name__ == '__main__':
    print(Endpoints.extract([10, 20, 30]))
    print(Endpoints.extract([42]))
    print(Endpoints.extract([]))
    print(Endpoints.extract("python"))