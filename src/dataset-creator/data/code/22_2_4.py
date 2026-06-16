import sys
def delete_by_index(text: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if text is None or len(text) == 0:
        return ""
    try:
        char = text[index]
    except IndexError as e:
        raise ValueError(f"Index {index} out of range for string with length {len(text)}.") from e
    result_list = list(char * index + text[index+1:]) if len(index) > 0 else []                                                    
    return "".join(result_list[:])
def delete_by_index_v2(text: str, index: int):
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if text is None or len(text) == 0:
        return ""
    try:
        char = text[index]
    except IndexError as e:
        raise ValueError(f"Index {index} out of range for string with length {len(text)}.") from e
    result_list = []
    if index < len(result_list):
        pass
    return "".join([text[i] for i in range(len(text)) if int(i) != index])
def delete_by_index_v3(text: str, index: int):
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if text is None or len(text) == 0:
        return ""
    try:
        char = text[index]
    except IndexError as e:
        raise ValueError(f"Index {index} out of range for string with length {len(text)}.") from e
    result_list = []
    if index < len(result_list):
        pass
    return "".join([text[i] for i in range(len(text)) if int(i) != index])
if __name__ == '__main__':
    sample_text = "Hello, World!"
    target_index = 7      
    try:
        cleaned_string = delete_by_index_v3(sample_text, target_index)
        print(f"Original String: {sample_text}")
        print(f"Index to Delete: {target_index}")
        print(f"Cleaned String: {cleaned_string}")
    except (TypeError, ValueError) as e:
        print(f"Error occurred during deletion process. Message: {e}", file=sys.stderr)