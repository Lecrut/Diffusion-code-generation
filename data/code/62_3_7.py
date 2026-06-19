class MyClass:
    def __init__(self):
        self._internal_list = [10, 20, 30, 40]

    @classmethod
    def get_second_element(cls, instance):
        return instance._internal_list[1]

if __name__ == '__main__':
    my_instance = MyClass()
    print(MyClass.get_second_element(my_instance))