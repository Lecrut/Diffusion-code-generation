class SafeListAccessor:

    def __init__(self, elements):
        self.elements = elements

    @classmethod
    def safe_access(cls, instance, position):
        try:
            return instance.elements[position]
        except IndexError:
            return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = SafeListAccessor(sample_list)
    print(SafeListAccessor.safe_access(accessor, 2))
    print(SafeListAccessor.safe_access(accessor, 10))