class SafeListAccess:

    def __init__(self, elements):
        self.elements = elements

    @classmethod
    def safe_access(cls, instance, position):
        if not isinstance(instance, cls):
            raise ValueError('Instance must be of type SafeListAccess')
        if not isinstance(position, int):
            raise ValueError('Position must be an integer')
        return instance.elements[position] if 0 <= position < len(instance.elements) else None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    safe_list_instance = SafeListAccess(sample_list)
    print(SafeListAccess.safe_access(safe_list_instance, 2))
    print(SafeListAccess.safe_access(safe_list_instance, 10))
    print(SafeListAccess.safe_access(safe_list_instance, -1))
    print(SafeListAccess.safe_access(safe_list_instance, 0))