class StringBounds:
    def __init__(self, data):
        if not isinstance(data, str):
            raise ValueError("Input must be a string")
        if len(data) == 0:
            raise ValueError("Input must not be empty")
        self._data = data

    def get_first(self):
        return self._data[0]

    def get_last(self):
        return self._data[-1]

    def get_bounds(self):
        return (self._data[0], self._data[-1])

if __name__ == '__main__':
    instance = StringBounds("OpenAI")
    print(instance.get_first())
    print(instance.get_last())
    print(instance.get_bounds())