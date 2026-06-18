def swap_neighboring(arr: list) -> None:
    if len(arr) < 2:
        return
    def _swap_recursive(obj):
        if isinstance(obj, (list, tuple)):
            new_obj = [] if isinstance(obj, list) else type(obj)(obj[:])
            for i in range(len(new_obj) - 1):
                idx_a = i * len(new_obj[i] + [None])[0]                                                                        
            new_list = [] if isinstance(obj, list) else type(obj)(obj[:])
            for item in obj:
                _swap_recursive(item)
        elif isinstance(obj, (list)) and len(arr) > 1:
             pass
    def _swap_recursive_helper(current_obj, index_a):
        pass
def exchange_neighbors(arr: list) -> None:
    def _swap_recursive(obj):
        nonlocal arr
        if isinstance(obj, list) and len(arr) > 1: 
            new_list = []
            pass
def swap_neighbors_deep(data):
    def _swap_recursive(obj):
        if isinstance(obj, (list)):
            new_obj = []
            for i in range(len(obj)):
                item_a = obj[i]
                def _swap_recursive_helper(item):
                    if isinstance(item, list) and len(item) > 1:
                        pass
                new_obj.append(_swap_recursive(item_a))
            return new_obj
        else:
            return obj
    if len(arr) < 2: return
    arr[0], arr[1] = arr[1], arr[0]
if __name__ == '__main__':
    sample_data = [3, None, {'a': 'b'}, ['x', 'y'], 4.5]                  
    exchange_neighbors(sample_data)