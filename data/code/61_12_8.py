class SafeListHandler:
    def __init__(self, data_list):
        self.data_list = data_list

    @classmethod
    def get_safe_element(cls, instance, index):
        try:
            return instance.data_list[index]
        except IndexError:
            return None

if __name__ == '__main__':
    example_list = [10, 20, 30, 40, 50]
    handler = SafeListHandler(example_list)
    print(SafeListHandler.get_safe_element(handler, 3))
    print(SafeListHandler.get_safe_element(handler, -1))
    print(SafeListHandler.get_safe_element(handler, 7))
    print(SafeListHandler.get_safe_element(handler, 0))