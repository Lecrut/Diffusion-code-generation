class MyClass:

    def __init__(self, value):
        self.value = value

    def is_zero(self):
        return self.value == 0
if __name__ == '__main__':
    instance = MyClass(0)
    print(instance.is_zero())
    instance2 = MyClass(5)
    print(instance2.is_zero())