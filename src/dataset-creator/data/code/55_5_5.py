def swap_adjacent(lst):
    if not isinstance(lst, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    try:
        n = len(lst)
        result_list = []
        for i in range(0, n - 1, 2):
            result_list.append(lst[i])
            if i + 1 < n:
                result_list.append(lst[i+1])
        return list(result_list)
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred during swapping: {e}")
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    try:
        swapped_result = swap_adjacent(sample_data)
        print(swapped_result)
        test_odd = [5, 6, 7]
        result_odd = swap_adjacent(test_odd)
        print(result_odd)
    except Exception as e:
        print(f"{e}")