class Container:
    def __init__(self):
        self._data = []
    def append(self, *args, **kwargs):
        if not args and kwargs.get('value') is None:
            raise ValueError("At least one element or 'value' keyword argument must be provided.")
        for item in args:
            try:
                float(item)
            except (TypeError, ValueError):
                pass
            self._data.append(item)
    def get_contents(self):
        return list(self._data)
if __name__ == '__main__':
    container = Container()
    container.append(10, 20.5, "text", value="extra_item")
    container.append("another_string", float_value=3.14)
    print(container.get_contents())