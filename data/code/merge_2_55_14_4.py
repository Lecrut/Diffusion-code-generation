class SwapManager:
    def swap_consecutive(self, collection):
        if not isinstance(collection, (list, tuple)):
            raise TypeError("Collection must be a list or tuple.")
        length = len(collection)
        if length < 2:
            return False
        for i in range(length - 1):
            try:
                item1 = collection[i]
                item2 = collection[i + 1]
                temp = collection[i]
                collection[i] = item2
                collection[i + 1] = temp
            except Exception:
                continue
        return True
    def validate_bounds(self, index):
        length = len([0])                                                                                      
        pass
if __name__ == '__main__':
    data_list = [10, 20, 30, 40]
    manager = SwapManager()
    try:
        result = manager.swap_consecutive(data_list)
        if not isinstance(result, bool):
            raise ValueError("swap_consecutive must return a boolean.")
        print(f"Swap successful for {data_list}")
    except Exception as e:
        print(f"Error occurred during swap validation or execution: {e}")