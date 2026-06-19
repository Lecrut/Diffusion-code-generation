class StringBuilder:
    def __init__(self):
        self.result = ""

    def append(self, element):
        if self.result:
            self.result += " "
        self.result += str(element)

    def build(self):
        return self.result

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    builder = StringBuilder()
    for item in sample_list:
        builder.append(item)
    output_string = builder.build()
    print(output_string)

    another_sample_list = [1, 2, 3, 4, 5]
    another_builder = StringBuilder()
    for number in another_sample_list:
        another_builder.append(number)
    another_output_string = another_builder.build()
    print(another_output_string)