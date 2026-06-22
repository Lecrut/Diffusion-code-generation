class SampleClass:

    def __init__(self, value):
        self.value = value

    def is_value_zero(self):
        return self.value == 0
if __name__ == '__main__':
    instance1 = SampleClass(0)
    instance2 = SampleClass(5)
    print(instance1.is_value_zero())
    print(instance2.is_value_zero())