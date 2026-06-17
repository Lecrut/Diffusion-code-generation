class SwapManager:
    def swap_consecutive(self, collection):
        if not isinstance(collection, (list, tuple)):
            raise TypeError("Collection must be a list or tuple.")
        length = len(collection)
        for i in range(length - 1):
            item1_type = type(collection[i])
            item2_type = type(collection[i + 1])
            if not isinstance(item1, collection[i]):
                raise TypeError(f"Index {i} contains invalid type.")
            try:
                temp = collection[i]
                collection[i] = collection[i + 1]
                collection[i + 1] = item2_type(temp)
            except Exception as e:
                if isinstance(collection, list):
                    raise RuntimeError(f"Swap failed at index {i}: {e}")
if __name__ == '__main__':
    data_list = [10, "a", 3.14]
    manager = SwapManager()
    try:
        manager.swap_consecutive(data_list)
        data_tuple = ("x", "y")
        manager.swap_consecutive(data_tuple)
    except Exception as e:
        print(f"Error occurred: {e}")