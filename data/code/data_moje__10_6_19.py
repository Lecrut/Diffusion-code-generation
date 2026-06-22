class ArrayProcessor:
    METADATA = {
        "label": "processor",
        "version": 1,
        "type": "list_handler"
    }

    def __init__(self, sequence):
        self.items = list(sequence)

    def get_first_element(self):
        if len(self.items) == 0:
            raise ValueError("Sequence is empty")
        return self.items[0]

    def get_metadata(self):
        return self.METADATA

if __name__ == '__main__':
    sample_list = [99, 88, 77, 66, 55]
    processor = ArrayProcessor(sample_list)
    first_item = processor.get_first_element()
    print(first_item)