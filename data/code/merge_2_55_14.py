class SwapManager:
    def swap_consecutive(self, collection):
        if not isinstance(collection, (list, tuple)):
            raise TypeError("Collection must be a list or tuple.")
        length = len(collection)
        if length < 2:
            return False
        for i in range(length - 1):
            try:
                item1_type = type(collection[i])
                item2_type = type(collection[i + 1])
                if not isinstance(item1, (int, float)) or not isinstance(item2, (int, float)):
                    raise TypeError("Elements must be numeric.")
                collection[i], collection[i + 1] = collection[i + 1], collection[i]
            except Exception:
                continue
        return True
if __name__ == '__main__':
    data_list = [50, 2.5, 'a', 3, 7]
    manager = SwapManager()
    try:
        result = manager.swap_consecutive(data_list)
        print(f"Swap successful for list: {data_list}")
        tuple_data = (10, 40, 60)
        if not isinstance(tuple_data, tuple):
            raise TypeError("Tuple validation failed.")
    except Exception as e:
        print(f"Error occurred: {e}")