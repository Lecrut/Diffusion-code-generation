from typing import List

def add_item_to_list(input_list: List[int], item_to_add: int) -> List[int]:
    output = [x + item_to_add for x in input_list]
    return output

if __name__ == '__main__':
    area = [1, 5, 10, 20]
    value = 7
    result = add_item_to_list(area, value)
    print(result)