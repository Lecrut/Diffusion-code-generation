class ArrayProcessor:
    def __init__(self, data_list):
        self.data_list = data_list

    def get_first_element(self):
        if len(self.data_list) > 0:
            return self.data_list[0]
        return None

if __name__ == '__main__':
    processor = ArrayProcessor([10, 20, 30])
    result = processor.get_first_element()
    print(result)