class SafeListAccess:

    def __init__(self, elements):
        self.elements = elements

    @staticmethod
    def safe_access(instance, position):
        if isinstance(position, int) and 0 <= position < len(instance.elements):
            return instance.elements[position]
        else:
            return None
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    safe_list_instance = SafeListAccess(sample_list)
    print(SafeListAccess.safe_access(safe_list_instance, 2))
    print(SafeListAccess.safe_access(safe_list_instance, 5))