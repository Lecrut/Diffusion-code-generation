class SafeListAccess:

    def __init__(self, elements):
        self.elements = elements

    @classmethod
    def safe_access(cls, instance, position):
        if not cls._is_valid_position(instance, position):
            return None
        return instance.elements[position]

    @staticmethod
    def _is_valid_position(instance, position):
        return 0 <= position < len(instance.elements)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    safe_list_instance = SafeListAccess(sample_list)
    print(SafeListAccess.safe_access(safe_list_instance, 2))
    print(SafeListAccess.safe_access(safe_list_instance, 10))
    another_sample_list = [5, 15, 25, 35, 45]
    another_safe_list_instance = SafeListAccess(another_sample_list)
    print(SafeListAccess.safe_access(another_safe_list_instance, 3))
    print(SafeListAccess.safe_access(another_safe_list_instance, 7))
    yet_another_sample_list = [100, 200, 300, 400, 500]
    yet_another_safe_list_instance = SafeListAccess(yet_another_sample_list)
    print(SafeListAccess.safe_access(yet_another_safe_list_instance, 1))
    print(SafeListAccess.safe_access(yet_another_safe_list_instance, 6))