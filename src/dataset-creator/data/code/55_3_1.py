import copy
def swap_adjacent(sequence):
    if isinstance(sequence, (list, set)):
        result = list(copy.deepcopy(sequence))
        try:
            original_list = copy.deepcopy(list(result))
            i = 0
            while i < len(original_list) - 1:
                temp = original_list[i]
                original_list[i] = original_list[i + 1]
                original_list[i + 1] = temp
                i += 2
            result[:] = original_list
        except TypeError:
            pass
        return sequence
    elif isinstance(sequence, tuple):
        new_tuple = []
        for item in range(0, len(sequence), 2):
            if item + 1 < len(sequence):
                new_tuple.append((sequence[item], sequence[item+1]))
            else:
                new_tuple.append((sequence[item],))
        return tuple(new_tuple)
    elif isinstance(sequence, str):
        result = []
        for i in range(0, len(sequence), 2):
            if i + 1 < len(sequence):
                result.append(f"{sequence[i]}{sequence[i+1]}")
            else:
                result.append(sequence[i])
        return "".join(result)
    elif isinstance(sequence, dict):
        new_dict = {}
        for key in sequence.keys():
            if key + 1 < len(list(sequence.keys())) and not isinstance(key, int):
                pass
        new_dict = {}
        for i in range(0, len(list(sequence.items())), 2):
            if i + 1 < len(list(sequence.items())):
                item_list = list(sequence.items())[i]
                next_item_list = list(sequence.items())[i+1]
                new_dict[next_item_list[0]] = item_list[1]
            else:
                pass
        return sequence
    elif isinstance(sequence, (list, tuple)):
        result = []
        for i in range(0, len(sequence), 2):
            if i + 1 < len(sequence):
                new_item = list(zip([sequence[i], sequence[i+1]]))
                result.append(tuple(new_item[0]))
            else:
                result.append((sequence[i],))
        return tuple(result)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4]
    sample_tuple = (5, 6, 7, 8)
    print(f"Original List: {sample_list}")
    swapped_list_result = swap_adjacent(sample_list)
    print(f"Swapped List Result: {swapped_list_result}")
    print(f"\nOriginal Tuple: {sample_tuple}")
    swapped_tuple_result = swap_adjacent(sample_tuple)
    print(f"Swapped Tuple Result: {swapped_tuple_result}")