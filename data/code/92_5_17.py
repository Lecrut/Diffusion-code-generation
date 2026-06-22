class TruthOpposer:
    _TRUE_MAP = {True: False, False: True}

    def __init__(self, data):
        self.data = data

    @staticmethod
    def _validate(item):
        if not isinstance(item, bool):
            raise ValueError("Only boolean values are allowed")
        return True

    def yield_opposites(self):
        for item in self.data:
            self._validate(item)
            yield self._TRUE_MAP[item]

if __name__ == '__main__':
    sample_values = [True, False, True, False, False]
    opposer = TruthOpposer(sample_values)
    result = list(opposer.yield_opposites())
    print(result)