class ElementAccess:
    def __init__(self, items):
        self._items = list(items)

    @classmethod
    def get_second(cls, instance):
        if len(instance._items) > 1:
            return instance._items[1]
        return None

if __name__ == '__main__':
    sample_items = [7, 14, 21, 28, 35]
    accessor = ElementAccess(sample_items)
    print(ElementAccess.get_second(accessor))

    short_items = [100]
    short_accessor = ElementAccess(short_items)
    print(ElementAccess.get_second(short_accessor))