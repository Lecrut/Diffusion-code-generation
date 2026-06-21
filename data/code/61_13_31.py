class SafeListAccess:

    def __init__(self, lst):
        self.lst = lst

    def get_element_at_index(self, index):
        if 0 <= index < len(self.lst):
            return self.lst[index]
        else:
            return None
if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    safe_access = SafeListAccess(sample_list)
    print(safe_access.get_element_at_index(2))
    print(safe_access.get_element_at_index(10))
    print(safe_access.get_element_at_index(-1))
    print(safe_access.get_element_at_index(0))