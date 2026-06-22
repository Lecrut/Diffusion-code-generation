class ValueInspector:
    DEFAULT_TRUTHY_SAMPLES = [0, 0, 0, 0]
    DEFAULT_FALSY_SAMPLES = [None, False, 0, ""]
    DEFAULT_MIXED_SAMPLES = [0, False, None, 1]

    @staticmethod
    def check_truthy_presence(data):
        if not hasattr(data, '__iter__'):
            raise ValueError("Input must be an iterable")
        return any(data)

if __name__ == '__main__':
    inspector = ValueInspector()
    print(inspector.check_truthy_presence(ValueInspector.DEFAULT_TRUTHY_SAMPLES))
    print(inspector.check_truthy_presence(ValueInspector.DEFAULT_FALSY_SAMPLES))
    print(inspector.check_truthy_presence(ValueInspector.DEFAULT_MIXED_SAMPLES))
    print(inspector.check_truthy_presence([0, 0, 1]))
    print(inspector.check_truthy_presence([]))