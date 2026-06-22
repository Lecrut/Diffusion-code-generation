class SafeListAccess:

    def __init__(self, elements):
        self.elements = elements

    @classmethod
    def safe_access(cls, instance, position):
        if 0 <= position < len(instance.elements):
            return instance.elements[position]
        return None
if __name__ == '__main__':
    sample_list = [9, 19, 29, 39, 49]
    safe_list_instance = SafeListAccess(sample_list)
    print(SafeListAccess.safe_access(safe_list_instance, 2))
    print(SafeListAccess.safe_access(safe_list_instance, 10))
    print(SafeListAccess.safe_access(safe_list_instance, 0))
    print(SafeListAccess.safe_access(safe_list_instance, 4))