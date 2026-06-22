import math

def get_middle_item(sequence):
    length = len(sequence)
    if length == 0:
        raise IndexError("Cannot get middle of empty sequence")
    
    if length % 2 == 1:
        middle_index = length // 2
        return sequence[middle_index]
    else:
        lower_index = (length // 2) - 1
        upper_index = length // 2
        lower_val = sequence[lower_index]
        upper_val = sequence[upper_index]
        
        if isinstance(lower_val, (int, float)) and isinstance(upper_val, (int, float)):
            return (lower_val + upper_val) / 2.0
        
        if isinstance(lower_val, str) and isinstance(upper_val, str):
            return lower_val + upper_val
        
        return [lower_val, upper_val]

if __name__ == '__main__':
    odd_list = [1, 2, 3, 4, 5]
    even_list = [1, 2, 3, 4]
    odd_str = "abcde"
    even_str = "abcd"
    single_item = [42]
    two_items = [10, 20]

    print(get_middle_item(odd_list))
    print(get_middle_item(even_list))
    print(get_middle_item(odd_str))
    print(get_middle_item(even_str))
    print(get_middle_item(single_item))
    print(get_middle_item(two_items))