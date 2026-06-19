class StringBuilder:
    def __init__(self):
        self.result = ""

    def append(self, element):
        if self.result:
            self.result += " "
        self.result += str(element)

    def get_result(self):
        return self.result

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    builder = StringBuilder()
    for item in sample_list:
        builder.append(item)
    print(builder.get_result())