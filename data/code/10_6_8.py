class ArrayProcessor:
    def __init__(self, data):
        self._data = data
        self._metadata = {
            "label": "primary_sequence",
            "version": 1
        }

    def get_first_element(self):
        if not self._data:
            raise ValueError("Data list cannot be empty")
        return self._data[0]

if __name__ == '__main__':
    sample_input = [5.5, 12.3, 9.8, 4.1, 7.2]
    instance = ArrayProcessor(sample_input)
    result = instance.get_first_element()
    print(result)