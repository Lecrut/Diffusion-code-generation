def get_last_element(sequence):
    if not sequence:
        raise ValueError("Input must be a non-empty list")
    return sequence[-1]

class ListProcessor:
    def __init__(self, data):
        self.data = data

    def get_tail(self):
        return get_last_element(self.data)

    def describe_tail(self):
        value = self.get_tail()
        return f"Last element: {value}"

if __name__ == '__main__':
    sample_data = [7, 14, 21, 28, 35]
    processor = ListProcessor(sample_data)
    print(processor.get_tail())
    print(processor.describe_tail())