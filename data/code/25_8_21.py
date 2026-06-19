class MyClass:

    def __init__(self, value):
        self.value = value

    def is_value_zero(self):
        return self.value == 0
if __name__ == '__main__':
    obj1 = MyClass(0)
    obj2 = MyClass(5)
    print(obj1.is_value_zero())
    print(obj2.is_value_zero())