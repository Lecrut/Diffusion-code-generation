class ElementAccessor:
    def __init__(self, data):
        self.data = data

    def access_elements(self):
        for index in range(len(self.data)):
            print(self.data[index])

if __name__ == '__main__':
    sample_values = [100, 200, 300, 400, 500]
    accessor = ElementAccessor(sample_values)
    accessor.access_elements()