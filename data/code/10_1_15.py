def _validate_list_arg(arg):
    if not isinstance(arg, list):
        raise TypeError("Argument must be a list")
    if len(arg) == 0:
        raise ValueError("List must not be empty")
    return arg

def get_first_element(lst):
    validated_list = _validate_list_arg(lst)
    first_index = 0
    return validated_list[first_index]

if __name__ == '__main__':
    fruits = ["mango", "orange", "grape", "kiwi"]
    first_item = get_first_element(fruits)
    print(first_item)