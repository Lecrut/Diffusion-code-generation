class SafeListAccess:
    def __init__(self, elements):
        self.elements = elements

    @classmethod
    def safe_access(cls, instance, position):
        if cls._is_valid_position(instance, position):
            return instance.elements[position]
        else:
            return None

    @staticmethod
    def _is_valid_position(instance, position):
        return 0 <= position < len(instance.elements)

if __name__ == '__main__':
    sample_list = [1000, 2000, 3000, 4000, 5000]
    safe_list_instance = SafeListAccess(sample_list)
    print(SafeListAccess.safe_access(safe_list_instance, 2))
    print(SafeListAccess.safe_access(safe_list_instance, 10))