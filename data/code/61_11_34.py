class SafeListAccess:

    def __init__(self, elements):
        self.elements = elements

    @classmethod
    def safe_access(cls, instance, position):
        try:
            return instance.elements[position]
        except IndexError:
            return None
if __name__ == '__main__':
    sample_values = [99, 199, 299, 399, 499]
    safe_list_instance = SafeListAccess(sample_values)
    print(SafeListAccess.safe_access(safe_list_instance, 0))
    print(SafeListAccess.safe_access(safe_list_instance, 3))
    print(SafeListAccess.safe_access(safe_list_instance, 5))