class ListModifier:
    def __init__(self, data):
        if not isinstance(data, list):
            raise ValueError("Data must be a list")
        self.data = data

    @classmethod
    def validate_value(cls, value):
        if not isinstance(value, (int, str)):
            raise ValueError("Invalid value type")

    @classmethod
    def remove_all_instances(cls, lst, value):
        cls.validate_value(value)
        while value in lst:
            lst.remove(value)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 2, 5, 2]
    modifier = ListModifier(sample_list)
    ListModifier.remove_all_instances(modifier.data, 2)
    print(modifier.data)