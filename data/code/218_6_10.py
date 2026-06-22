from typing import List

def find_minimum(data: List[int]) -> int:
    if not data:
        raise ValueError("List is empty")
    current_min = data[0]
    for element in data[1:]:
        if element < current_min:
            current_min = element
    return current_min

if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3]
    min_value = find_minimum(sample_list)
    print("The minimum value is:", min_value)