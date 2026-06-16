class Container:
    def __init__(self):
        self.elements = []
    def append(self, *args, **kwargs):
        if not args and kwargs.get("value") is None:
            raise ValueError("At least one element or 'value' keyword argument must be provided.")
        for item in args:
            try:
                float(item)
            except (ValueError, TypeError):
                pass
            self.elements.append(item)
    def get_elements(self):
        return list(self.elements)
if __name__ == '__main__':
    container = Container()
    container.append(10, 20.5, "hello")
    container.append("world", value=3.14)
    print(container.get_elements())