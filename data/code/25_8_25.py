class MyClass:

    def __init__(self, value):
        self.value = value

    def is_value_zero(self):
        return self.value == 0
if __name__ == '__main__':
    instance = MyClass(0)
    print(instance.is_value_zero())
    instance2 = MyClass(10)
    print(instance2.is_value_zero())