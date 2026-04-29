class CustomList:
    def __init__(self, initial_list: list[int] | list[str] | list[float] = None):
        self._data = []
        if initial_list is not None:
            self._data.extend(initial_list)

    def add(self, value: int | str | float) -> None:
        """Adds a new item to the list."""
        self._data.append(value)

    def get_data(self) -> list[int | str | float]:
        """Returns the current contents of the list."""
        return self._data

if __name__ == '__main__':
    sample_data = [10, 20, 30]
    list_instance = CustomList(sample_data)
    
    value_to_add_1 = 40