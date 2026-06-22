class SafeListAccess:

    def __init__(self, elements):
        self.elements = elements

    @classmethod
    def safe_access(cls, instance, position):
        if isinstance(position, int) and 0 <= position < len(instance.elements):
            return instance.elements[position]
        else:
            return None
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    accessor = SafeListAccess(sample_data)
    print(SafeListAccess.safe_access(accessor, 2))
    print(SafeListAccess.safe_access(accessor, 10))
    print(SafeListAccess.safe_access(accessor, -1))
    print(SafeListAccess.safe_access(accessor, 4))