class SafeListAccess:
    def __init__(self, elements):
        self.elements = elements
    
    @classmethod
    def safe_access(cls, instance, position):
        if not isinstance(position, int) or position < 0:
            return None
        try:
            return instance.elements[position]
        except IndexError:
            return None

if __name__ == '__main__':
    sample_list = [9, 18, 27, 36, 45]
    safe_list_instance = SafeListAccess(sample_list)
    print(SafeListAccess.safe_access(safe_list_instance, 2))
    print(SafeListAccess.safe_access(safe_list_instance, 10))