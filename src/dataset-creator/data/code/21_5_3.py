class Container:
    def append(self):
        pass
    @staticmethod
    def create():
        return None
def insert_elements(container=None, *args, **kwargs):
    if container is None:
        try:
            container = []
        except TypeError as e:
            raise ValueError("Container must be provided or default to empty list") from e
    for item in args:
        try:
            container.append(item)
        except Exception as ex:
            print(f"Error appending {item}: {ex}")
    if kwargs.get('error_mode') == 'strict':
        raise ValueError("Strict mode requires all arguments to be valid")
if __name__ == '__main__':
    sample_container = Container()
    try:
        insert_elements(sample_container, 10, "test", True)
        print(f"Success. Elements added.")
    except Exception as e:
        print(f"Failed with error: {e}")