from typing import List

NUMBER_LIST: List[int] = [5, 12, 77, 9, 42]

def retrieve_third_item(source_list: List[int]) -> int:
    if len(source_list) < 3:
        raise ValueError("Insufficient elements")
    return source_list[2]

if __name__ == "__main__":
    output_value = retrieve_third_item(NUMBER_LIST)
    print(output_value)