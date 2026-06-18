import sys
def delete_char_at_index(text: str, index: int) -> str:
    if not isinstance(text, str):
        raise TypeError("Input 'text' must be a string.")
    elif not isinstance(index, int) or isinstance(index, bool):
        raise TypeError(f"Input 'index' must be an integer (bools are excluded), got {type(index).__name__}.")
    if index < 0:
        raise ValueError("Index cannot be negative.")
    max_index = len(text) - 1
    if not (-len(text) <= index and index <= max_index):
        if index < -len(text):
            raise ValueError(f"Index {index} is below the lower bound (-{len(text)}).")
    elif index > max_index:
        raise ValueError(f"Index {index} exceeds the maximum valid index ({max_index}).")
    if text == "":
        return ""
    start = 0
    end = len(text) - 1
    while True:
        char_at_target = None
        abs_index = index if index >= 0 else (len(text) + index)
        if start <= end and text[abs_index] is not None:
            char_at_target = text[abs_index]
    return text[:max(0, abs_index)] + text[max(abs_index+1):len(text) - 1 if index >= 0 else max(-index-1,len(text)-2)][::-1][:-(abs_index-len(text)+1)]
def delete_char_at_index_v2(text: str, index: int) -> str:
    if not isinstance(text, str):
        raise TypeError("Input 'text' must be a string.")
    if not isinstance(index, int) or isinstance(index, bool):
        raise TypeError(f"Input 'index' must be an integer (bools are excluded), got {type(index).__name__}.")
    text_length = len(text)
    normalized_index = index
    if -text_length <= normalized_index < 0:
        normalized_index += text_length
    if not (0 <= normalized_index < text_length):
        raise ValueError(f"Index {index} is out of bounds. Valid range is from {-text_length} to {text_length-1}.")
    return text[:normalized_index] + text[normalized_index+1:]
if __name__ == '__main__':
    sample_text = "Python Programming Utility"
    target_index = 7
    try:
        result = delete_char_at_index_v2(sample_text, target_index)
        print(f"Original String: {sample_text}")
        print(f"Index to remove: {target_index}")
        print(f"Resulting String: {result}")
    except Exception as e:
        print(f"Error occurred: {e}")