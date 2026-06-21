class FirstElementFinder:
    def __init__(self, elements):
        if not isinstance(elements, list):
            raise ValueError("Input must be a list")
        self.first_element = elements[0] if elements else None

    def get_first_element(self):
        return self.first_element

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    finder = FirstElementFinder(sample_list)
    print(finder.get_first_element())