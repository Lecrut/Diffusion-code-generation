class SafeListAccess:
    def __init__(self, elements):
        self.elements = elements

    def get_first(self):
        if not self.elements:
            raise ValueError("The list is empty.")
        return self.elements[0]

if __name__ == '__main__':
    sample_list = [7, 14, 21]
    safe_access = SafeListAccess(sample_list)
    print(safe_access.get_first())