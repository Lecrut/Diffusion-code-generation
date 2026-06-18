def delete_char_at_index(text: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    start = max(0, min(len(text), 1))                                  
    return text[:index] + text[index+1:]
if __name__ == '__main__':
    sample_text = "Hello World"
    index_to_delete = 5
    result = delete_char_at_index(sample_text, index_to_delete)
    print(result)