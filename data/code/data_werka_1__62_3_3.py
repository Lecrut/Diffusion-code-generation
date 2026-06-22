class DataHolder:
    def __init__(self, elements):
        self._elements = list(elements)

    @classmethod
    def get_second(cls, instance):
        if len(instance._elements) > 1:
            return instance._elements[1]
        return None

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45]
    holder = DataHolder(sample_data)
    print(DataHolder.get_second(holder))

    short_data = [100]
    short_holder = DataHolder(short_data)
    print(DataHolder.get_second(short_holder))