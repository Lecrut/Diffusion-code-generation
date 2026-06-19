class ElementAccessor:
    _DEFAULT_LIST = [100, 200, 300, 400]

    def __init__(self, data=None):
        if data is None:
            self._internal_list = self._DEFAULT_LIST
        else:
            self._internal_list = list(data)

    @classmethod
    def get_second_element(cls, instance):
        if len(instance._internal_list) > 1:
            return instance._internal_list[1]
        return None

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    accessor = ElementAccessor(sample_data)
    result = ElementAccessor.get_second_element(accessor)
    print(result)

    default_accessor = ElementAccessor()
    default_result = ElementAccessor.get_second_element(default_accessor)
    print(default_result)

    short_data = [5]
    short_accessor = ElementAccessor(short_data)
    short_result = ElementAccessor.get_second_element(short_accessor)
    print(short_result)