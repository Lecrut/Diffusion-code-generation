class SampleClass:

    def __init__(self, attribute):
        self.attribute = attribute

    def is_attribute_zero(self):
        return self.attribute == 0
if __name__ == '__main__':
    sample_instance = SampleClass(0)
    print(sample_instance.is_attribute_zero())