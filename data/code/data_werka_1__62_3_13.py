class ElementAccessor:
    def __init__(self, data):
        self._data_list = list(data)

    @classmethod
    def fetch_second(cls, instance):
        if len(instance._data_list) > 1:
            return instance._data_list[1]
        return None

if __name__ == '__main__':
    sample_values = ['apple', 'banana', 'cherry', 'date']
    accessor_instance = ElementAccessor(sample_values)
    second_element = ElementAccessor.fetch_second(accessor_instance)
    print(second_element)

    short_sample = [42]
    short_accessor_instance = ElementAccessor(short_sample)
    second_of_short = ElementAccessor.fetch_second(short_accessor_instance)
    print(second_of_short)