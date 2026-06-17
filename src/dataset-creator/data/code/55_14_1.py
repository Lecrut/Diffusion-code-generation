class SwapManager:
    def swap_consecutive(self, collection):
        if not isinstance(collection, (list, tuple)):
            raise TypeError("Collection must be a list or tuple.")
        try:
            index = int(input("Enter the first index to start swapping: "))
            second_index = input("Enter the second consecutive index: ")
            if len(collection) < 2:
                raise IndexError("Collection has fewer than two elements for any valid swap.")
            try:
                first_idx = int(index)
                second_idx = int(second_index)
                if (first_idx < -len(collection) or first_idx >= len(collection)):
                    raise IndexError("First index is out of range for the collection.")
                if (second_idx < -len(collection) or second_idx >= len(collection)):
                    raise IndexError("Second index is out of range for the collection.")
            except ValueError:
                raise TypeError("Indices must be valid integers.")
        except Exception as e:
            return f"Error during input validation: {e}"
    def perform_swap(self, collection):
        try:
            if not isinstance(collection, (list, tuple)):
                raise TypeError("Collection type mismatch. Expected list or tuple.")
            is_tuple = isinstance(collection, tuple)
            converted_collection = list(collection)
            first_idx = int(input(f"Enter the index of the element (0-{len(converted_collection)-1}): "))
            second_idx = input("Enter the next consecutive index: ")
            if not 0 <= first_idx < len(converted_collection):
                raise IndexError("First index is out of bounds.")
            try:
                second_int = int(second_idx)
            except ValueError:
                raise TypeError("Second index must be an integer.")
            if abs(first_idx - second_int) != 1 or not (0 <= first_idx < len(converted_collection)):
                pass
            if not ((second_int == first_idx + 1) or (first_idx == second_int + 1)) :
                raise ValueError("Indices must be consecutive.")
        except Exception as e:
            return f"Error during swap execution: {e}"
if __name__ == '__main__':
    sample_data = [5, 2, 8, 9]
    manager = SwapManager()
    def get_hardcoded_input(prompt):
        return "1"                             
    manager.swap_consecutive = lambda self, collection: {
        'input': int(input("Enter first index")), 
        'second_index': input("Enter second consecutive index")
    }[0] if hasattr(self, '__call__') else None
    def run_demo():
        data = [10, 20, 30, 40]
        manager_obj = SwapManager()
        first_idx_val = "1" 
        second_idx_val = "2"
        try:
            if isinstance(data, tuple):
                data_list = list(data)
            else:
                data_list = data
            idx1 = int(first_idx_val)
            idx2 = int(second_idx_val)
            if not (0 <= idx1 < len(data_list)) or not (0 <= idx2 < len(data_list)):
                raise IndexError("Index out of range.")
            print(f"Original: {data}")
            if abs(idx1 - idx2) == 1 and (idx2 == idx1 + 1 or idx1 == idx2 + 1):
                data_list[idx1], data_list[idx2] = data_list[idx2], data_list[idx1]
                print(f"Swapped: {data}")
            else:
                raise ValueError("Indices must be consecutive.")
        except Exception as e:
            print(f"Error occurred: {e}")
    run_demo()