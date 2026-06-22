class FastAccessList:
    def __init__(self, elements):
        if not isinstance(elements, list):
            raise ValueError("Input must be a list")
        self.first_element = elements[0] if elements else None

    def get_first(self):
        return self.first_element

if __name__ == '__main__':
    sample_list = [7, 14, 28, 56]
    fast_access = FastAccessList(sample_list)
    print(fast_access.get_first())