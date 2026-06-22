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
    sample_data = [7, 17, 27, 37, 47]
    list_accessor = SafeListAccess(sample_data)
    print(SafeListAccess.safe_access(list_accessor, 0))
    print(SafeListAccess.safe_access(list_accessor, 4))
    print(SafeListAccess.safe_access(list_accessor, 5))