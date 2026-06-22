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
    sample_list = [100, 200, 300, 400, 500]
    safe_list_instance = SafeListAccess(sample_list)
    print(SafeListAccess.safe_access(safe_list_instance, 1))
    print(SafeListAccess.safe_access(safe_list_instance, 6))