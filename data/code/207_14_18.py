class FloatListProcessor:
    MAX_LIST_SIZE = 1000

    @staticmethod
    def find_maximum(data):
        if not data:
            raise ValueError("Data list is empty")
        if len(data) > FloatListProcessor.MAX_LIST_SIZE:
            raise ValueError("Data list exceeds maximum allowed size")
        return max(data)

if __name__ == '__main__':
    sample_list = [10.5, 5.2, 20.8, 8.9, 15.3]
    processor = FloatListProcessor()
    maximum_value = processor.find_maximum(sample_list)
    print(maximum_value)