class SecondToLastExtractor:
    def __init__(self, data):
        self.data = data

    def get_second_to_last(self):
        if len(self.data) < 2:
            raise IndexError("Insufficient elements to retrieve the second-to-last item.")
        return self.data[-2]

    def get_second_to_last_safe(self):
        if len(self.data) < 2:
            return None
        return self.data[-2]

if __name__ == '__main__':
    values = [100, 200, 300, 400, 500]
    processor = SecondToLastExtractor(values)
    print(processor.get_second_to_last())
    print(processor.get_second_to_last_safe())
    short_list = [42]
    short_processor = SecondToLastExtractor(short_list)
    print(short_processor.get_second_to_last_safe())
    try:
        short_processor.get_second_to_last()
    except IndexError as e:
        print(str(e))