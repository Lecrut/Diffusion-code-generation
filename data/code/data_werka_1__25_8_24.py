class MyClass:

    def __init__(self, value):
        self.value = value

    def is_value_zero(self):
        return self.value == 0
if __name__ == '__main__':
    instance = MyClass(0)
    print(instance.is_value_zero())
    another_instance = MyClass(5)
    print(another_instance.is_value_zero())