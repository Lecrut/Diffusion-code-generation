class FirstElementFinder:
    def __init__(self, elements):
        self.first_element = None
        if elements:
            self.first_element = elements[0]

    def get_first_element(self):
        return self.first_element

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    finder = FirstElementFinder(sample_list)
    print(finder.get_first_element())