from typing import Any, List

def retrieve_final_item(sequence: List[Any]) -> Any:
    if not isinstance(sequence, list):
        raise TypeError("Argument must be a list")
    if len(sequence) < 1:
        raise ValueError("Sequence cannot be empty")
    return sequence[-1]

if __name__ == '__main__':
    data_set = [7, 14, 21, 28, 35]
    last_val = retrieve_final_item(data_set)
    print(last_val)
    text_set = ["alpha", "beta", "gamma"]
    last_text = retrieve_final_item(text_set)
    print(last_text)