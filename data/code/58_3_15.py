class ListAccessor:
    @staticmethod
    def get_first_element(data):
        return data[0]

if __name__ == '__main__':
    sample_data = [15, 30, 45]
    first_element = ListAccessor.get_first_element(sample_data)
    print(first_element)