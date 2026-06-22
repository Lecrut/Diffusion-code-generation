class StringBoundary:
    _FIRST_INDEX = 0
    _LAST_INDEX = -1

    def __init__(self, items):
        if not items:
            raise ValueError("Sequence must contain at least one item")
        self.items = items

    @staticmethod
    def get_bounds(items):
        if not items:
            raise ValueError("Sequence must contain at least one item")
        return items[StringBoundary._FIRST_INDEX], items[StringBoundary._LAST_INDEX]

    def retrieve(self):
        return StringBoundary.get_bounds(self.items)

if __name__ == '__main__':
    sample_data = ["start", "middle", "end"]
    boundary = StringBoundary(sample_data)
    first, last = boundary.retrieve()
    print(first)
    print(last)