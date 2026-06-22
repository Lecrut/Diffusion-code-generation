class ListProcessor:
    def __init__(self, data):
        self.data = data

    def get_middle(self):
        length = len(self.data)
        if length == 0:
            raise ValueError("List must not be empty")
        mid = length // 2
        if length % 2 == 0:
            left = self.data[mid - 1:mid]
            right = self.data[mid:mid + 1]
            return (left[0] + right[0]) / 2.0
        return self.data[mid]

    def get_middle_element(self):
        return self.get_middle()

if __name__ == '__main__':
    odd_data = [1, 2, 3, 4, 5]
    even_data = [10, 20, 30, 40]
    processor_odd = ListProcessor(odd_data)
    processor_even = ListProcessor(even_data)
    print(processor_odd.get_middle())
    print(processor_even.get_middle_element())