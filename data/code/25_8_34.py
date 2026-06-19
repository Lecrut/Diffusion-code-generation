class MyClass:

    def __init__(self, value):
        self.value = value

    @classmethod
    def is_value_zero(cls, instance):
        return instance.value == 0
if __name__ == '__main__':
    obj1 = MyClass(0)
    obj2 = MyClass(5)
    print(MyClass.is_value_zero(obj1))
    print(MyClass.is_value_zero(obj2))