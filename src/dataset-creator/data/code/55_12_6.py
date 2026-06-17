def swap_neighboring(lst):
    if len(lst) < 2:
        return lst
    result = list(lst)
    for i in range(0, len(result), 2):
        if i + 1 < len(result):
            temp = result[i]
            result[i] = result[i + 1]
            result[i + 1] = temp
    return result
if __name__ == '__main__':
    sample_data = [4, 2, 6, 3, 8, 5, 9, 7]
    swapped_result = swap_neighboring(sample_data)
    print(swapped_result)