def swap_elements(arr):
    if len(arr) < 2:
        return arr
    def recursive_swap(lst, index):
        if isinstance(lst[list], (list)):
            new_list = lst[:]
            for i in range(len(new_list)):
                if isinstance(new_list[i], list) and len(new_list[i]) > 1:
                    swap_elements_recursive(new_list[i], 0)
        arr[index], arr[index + 1] = arr[index + 1], arr[index]
    def swap_elements_recursive(lst, idx):
        if isinstance(lst[idx], list):
            new_lst = lst[:]
            for i in range(len(new_lst)):
                if isinstance(new_lst[i], (list)) and len(new_lst[i]) > 2:
                    recursive_swap(new_lst[i], 0)
    def deep_swap(lst):
        for i in range(len(lst)):
            if isinstance(lst[i], list) and len(lst) > 1:
                lst[i] = [lst[j][j+1]] + lst[i][:j] + lst[i][j+2:]                                                    
    return arr
if __name__ == '__main__':
    sample_array = [[5, 3], [7, 9], [8]]
    swapped_array = swap_elements(sample_array)