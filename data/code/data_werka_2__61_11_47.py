class SafeListAccess:

    def __init__(self, elements):
        self.elements = elements

    @classmethod
    def safe_access(cls, instance, position):
        if 0 <= position < len(instance.elements):
            return instance.elements[position]
        return None
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    safe_list_instance = SafeListAccess(sample_list)
    print(SafeListAccess.safe_access(safe_list_instance, 2))
    print(SafeListAccess.safe_access(safe_list_instance, 5))