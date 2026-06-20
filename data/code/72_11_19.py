class ElementComparator:
    @staticmethod
    def is_greater(data):
        if not (0 <= 0 < len(data) and 0 <= 5 < len(data)):
            raise IndexError("Index out of bounds")
        return data[0] > data[5]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(ElementComparator.is_greater(sample_list))