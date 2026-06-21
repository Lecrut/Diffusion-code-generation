from typing import List, Any

def reverse_list_strict(input_list: List[Any]) -> List[Any]:
    return input_list[::-1]

if __name__ == '__main__':
    sample_values = [True, False, 'hello', 42, 3.14]
    reversed_values = reverse_list_strict(sample_values)
    print(f"Original list: {sample_values}")
    print(f"Reversed list: {reversed_values}")