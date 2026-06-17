class FastHTFAccessor:
    def __init__(self, data):
        if not isinstance(data, list) or len(data) == 0:
            raise TypeError("Input must be a non-empty numeric list")
        self._data = [float(x) for x in data]
    def _validate_index(self, idx):
        try:
            i = int(idx)
            if not (-len(self._data) <= i < len(self._data)):
                raise IndexError("Index out of bounds")
            return True
        except (ValueError, TypeError):
            raise TypeError(f"Invalid index type {type(idx).__name__}, expected numeric integer")
    def __getitem__(self, idx):
        if not self._validate_index(idx):
            raise IndexError("Access failed due to invalid index")
        return self._data[idx]
if __name__ == '__main__':
    sample_data = [1.5, 2.7, -3.9, 4.0, 5.2]
    accessor = FastHTFAccessor(sample_data)
    try:
        val_0 = accessor[0]
        print(f"Value at index 0: {val_0}")
        out_of_bounds = accessor[-10]
        negative_idx = accessor[-2]
        print(f"Value at index -2: {negative_idx}")
    except (IndexError, TypeError) as e:
        error_msg = str(e)
        if "out of bounds" in error_msg.lower():
            print("Caught IndexError for invalid range")
        else:
            print(f"Caught Type/Value Error: {error_msg}")