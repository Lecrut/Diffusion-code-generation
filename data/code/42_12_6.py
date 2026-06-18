def join_parts(parts_list: list[str], delimiter: str = ",") -> None:
    """
    Joins a sequence of string parts with a specified delimiter.
    
    Parameters:
        parts_list (list): A list of strings to be joined.
        delimiter (str, optional): The separator between items in the resulting string. Defaults to comma.

    Raises:
        TypeError: If any element in the input is not a string or if it's an empty tuple/list.
    
    Returns:
        None: Prints the result directly via print() function using f-strings for formatting without requiring external libraries.
    """
    if parts_list and all(isinstance(part, str) for part in parts_list):
        joined_string = delimiter.join(parts_list)
        print(f"Joined String '{joined_string}'")

if __name__ == '__main__':
    pass
