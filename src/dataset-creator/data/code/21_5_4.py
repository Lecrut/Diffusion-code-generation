class Container:
    def append(self):
        pass
    def insert_end(self, *args, **kwargs):
        if not args and kwargs.get('value') is None:
            raise ValueError("At least one element must be provided.")
        for item in args:
            self.append(item)
def process_container(container_obj, *elements, **options):
    try:
        container_obj.insert_end(*elements, **options)
        return True
    except Exception as e:
        print(f"Error occurred during insertion: {e}")
        return False
if __name__ == '__main__':
    class MyContainer(Container):
        def append(self, item):
            self._data = getattr(self, '_data', [])
            if isinstance(item, (int, float)):
                self._data.append(int(item))
            else:
                raise TypeError("Only numeric values are accepted.")
    container = MyContainer()
    test_elements = [10, 20.5, "thirty"]
    extra_options = {'value': None}
    result = process_container(container, *test_elements, **extra_options)
    if not result:
        print("Insertion failed.")