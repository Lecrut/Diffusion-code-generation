class FirstElementExtractor:
    def __init__(self, data):
        self.data = data

    def extract(self):
        if not isinstance(self.data, list) or len(self.data) < 1:
            raise ValueError("Input must be a non-empty list")
        if not all(isinstance(item, int) for item in self.data):
            raise ValueError("All items must be integers")
        return self.data[0]

def get_first_element_from_list(sample_list):
    extractor = FirstElementExtractor(sample_list)
    return extractor.extract()

if __name__ == '__main__':
    sample_integers = [42, 17, 99, 3]
    result = get_first_element_from_list(sample_integers)
    print(result)