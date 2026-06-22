class ListAccessor:
    def __init__(self, data):
        self.data = data

    def get_first_element(self):
        return self.data[0]

if __name__ == '__main__':
    sample_data = [99, 198, 297]
    accessor = ListAccessor(sample_data)
    print(accessor.get_first_element())