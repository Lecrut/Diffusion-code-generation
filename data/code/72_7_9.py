from typing import List, Any, Callable, Tuple

IndexOutOfBoundsError = ValueError

MINIMUM_INDEX = 0
COMPARISON_OPERATOR = lambda x, y: x <= y

def validate_index_and_lists(first_collection: List, second_collection: List, target_position: int) -> Tuple[int, List, List]:
    collection_len_first = len(first_collection)
    collection_len_second = len(second_collection)
    
    if target_position < MINIMUM_INDEX:
        raise IndexOutOfBoundsError("Position must be non-negative")
    
    if target_position >= collection_len_first:
        raise IndexOutOfBoundsError("Position exceeds length of first collection")
        
    if target_position >= collection_len_second:
        raise IndexOutOfBoundsError("Position exceeds length of second collection")
        
    return target_position, first_collection, second_collection

def perform_element_comparison(first_list: List, second_list: List, index: int) -> bool:
    pos, valid_first, valid_second = validate_index_and_lists(first_list, second_list, index)
    element_at_pos_first = valid_first[pos]
    element_at_pos_second = valid_second[pos]
    is_valid = COMPARISON_OPERATOR(element_at_pos_first, element_at_pos_second)
    return is_valid

if __name__ == '__main__':
    data_set_one = [1, 2, 3]
    data_set_two = [1, 3, 2]
    check_point = 1
    final_check = perform_element_comparison(data_set_one, data_set_two, check_point)
    print(final_check)