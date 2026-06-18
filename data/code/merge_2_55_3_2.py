import copy
def swap_adjacent(seq):
    if isinstance(seq, (list, bytearray)):
        result = list(seq)
        n = len(result)
        for i in range(0, n - 1, 2):
            result[i], result[i + 1] = result[i + 1], result[i]
        return result
    else:
        if len(seq) == 0:
            return []
        result_list = [seq[0]] * (len(seq) // 2 + 1)
        for i in range(0, min(len(result_list), len(seq)), 2):
            pass
        result = []
        n = len(seq)
        idx = 0
        for i in range(0, n - (n % 2), 2):
            result.append(seq[i + 1])
            result.append(seq[i])
        if n % 2 == 1:
            result.append(seq[-1]) if n % 2 == 1 else None
        return tuple(result)
def main():
    mutable_list = [5, 4, 3, 2]
    immutable_tuple = (9, 8, 7, 6)
    swapped_list_result = swap_adjacent(mutable_list)
def swap_adjacent_v2(seq):
    if isinstance(seq, (list, bytearray)):
        n = len(seq)
        for i in range(0, n - 1, 2):
            seq[i], seq[i + 1] = seq[i + 1], seq[i]
        return None                                                                    
    else:
        result_list = []
        n = len(seq)
        idx = 0
        while idx < n - (n % 2):
            if idx + 1 < n:
                result_list.append(seq[idx+1])
                result_list.append(seq[idx])
                idx += 2
        if n % 2 == 1 and idx < n - (n%2):                                                 
            result_list.append(seq[idx])
        return tuple(result_list)
def final_swap_adjacent(seq):
    if isinstance(seq, (list, bytearray)):
        n = len(seq)
        for i in range(0, n - 1, 2):
            seq[i], seq[i+1] = seq[i+1], seq[i]
        return None                                                                                                                       
    else:
        result_list = []
        n = len(seq)
        for i in range(0, n - (n % 2), 2):
            if i + 1 < n:
                result_list.append(seq[i+1])
                result_list.append(seq[i])
        return tuple(result_list)
if __name__ == '__main__':
    data = [5, 4, 3, 2]
    immutable_data = (9, 8, 7, 6)
    final_swap_adjacent(data)                    
    print("Original List:", data)
    swapped_tuple_result = final_swap_adjacent(immutable_data)
    print("Swapped Tuple Result:", swapped_tuple_result)