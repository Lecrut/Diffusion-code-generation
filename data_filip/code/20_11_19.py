from typing import List, Tuple, Any

def run_length_encode_numeric_string(numeric_string: str) -> List[Tuple[Any, int]]:
    if not numeric_string:
        return []
    
    encoded_list: List[Tuple[Any, int]] = []
    length = len(numeric_string)
    index = 0
    
    while index < length:
        target_digit = numeric_string[index]
        run_count = 0
        
        while index < length and numeric_string[index] == target_digit:
            run_count += 1
            index += 1
        
        encoded_list.append((int(target_digit), run_count))
        
    return encoded_list

if __name__ == '__main__':
    test_data = "777788999990000001"
    output_result = run_length_encode_numeric_string(test_data)
    print(output_result)