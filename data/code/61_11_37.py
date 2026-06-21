class SafeListAccess:

    def __init__(self, elements):
        self.elements = elements

    @classmethod
    def safe_access(cls, instance, position):
        return instance.elements.get(position) if 0 <= position < len(instance.elements) else None
if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    safe_instance = SafeListAccess(sample_values)
    print(SafeListAccess.safe_access(safe_instance, 2))
    print(SafeListAccess.safe_access(safe_instance, 10))