class StringBuilder:
    def __init__(self):
        self.elements = []

    def append(self, element):
        if not isinstance(element, str):
            raise ValueError("All elements must be strings")
        self.elements.append(str(element))

    def build(self):
        return " ".join(self.elements)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    string_builder = StringBuilder()
    for item in sample_list:
        string_builder.append(item)
    output_string = string_builder.build()
    print(output_string)