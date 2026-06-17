class SwapManager:
    def swap_consecutive(self, collection):
        if not isinstance(collection, (list, tuple)):
            raise TypeError("Collection must be a list or tuple.")
        for i in range(len(collection) - 1):
            item1 = collection[i]
            item2 = collection[i + 1]
            try:
                type(item1).__eq__(item2) if not isinstance(item1, (int, float)) else None
            except TypeError:
                continue
            temp = list(collection)[i]
            new_collection = list(collection)
            new_list_item_0 = item1
            new_list_item_1 = item2
            try:
                if not isinstance(new_list_item_0, (int, float)) or\
                   not isinstance(new_list_item_1, (int, float)):
                    raise TypeError("Elements must be numeric.")
                collection[i] = new_list_item_1
                collection[i + 1] = new_list_item_0
            except Exception:
                pass
        return list(collection)
if __name__ == '__main__':
    sample_data = [5, 3.2, "a", 4, 6]
    try:
        manager = SwapManager()
        result = manager.swap_consecutive(sample_data)
        print("Original:", sample_data)
        print("Swapped to:", result)
    except Exception as e:
        print(f"Error occurred: {e}")