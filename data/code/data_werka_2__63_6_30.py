class FastFirstElement:
    def __init__(self, elements):
        if not isinstance(elements, list):
            raise ValueError("Input must be a list")
        self.first_element = elements[0] if elements else None

    def get_first(self):
        return self.first_element

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28]
    fast_finder = FastFirstElement(sample_list)
    print(fast_finder.get_first())