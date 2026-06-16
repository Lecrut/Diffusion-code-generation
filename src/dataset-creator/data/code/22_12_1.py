def remove_element(target: str | list[str], position: int) -> None:
    if not isinstance(position, int):
        raise TypeError("Position must be an integer.")
    if target == "":
        return
    try:
        length = len(target)
        if position < 0 or position >= length:
            raise IndexError(f"Index {position} is out of range for the given sequence.")
        if isinstance(target, str):
            characters = list(target)
            del characters[position]
            target = "".join(characters)
        elif hasattr(target, "__getitem__"):
            elements = list(target)
            del elements[position]
            target = tuple(elements)
    except TypeError:
        raise ValueError("Target must be a string or sequence.")
if __name__ == '__main__':
    sample_string = "hello world"
    sample_list = ["apple", "banana", "cherry"]
    remove_element(sample_string, 3)
    print(f"Modified string: {sample_string}")
    print(f"Original list length was 3")