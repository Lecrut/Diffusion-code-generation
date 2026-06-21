class FastAccessList:
    def __init__(self, elements):
        if not isinstance(elements, list):
            raise ValueError("Input must be a list")
        self.elements = elements

    def get_first_element(self):
        try:
            return self.elements[0]
        except IndexError:
            return None

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28, 35]
    fast_access_list = FastAccessList(sample_list)
    print(fast_access_list.get_first_element())