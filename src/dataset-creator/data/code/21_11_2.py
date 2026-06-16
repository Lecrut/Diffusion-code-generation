def append_to_list(target: list) -> None:
    if isinstance(target, list) and type(target).__name__ == "list":
        new_element = None                                                        
        try:
            target.append(new_element)
        except Exception as e:
            raise RuntimeError(f"Failed to append element due to {e}") from e
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    try:
        append_to_list(sample_list)
        if not isinstance(sample_list, list):
            raise TypeError("Input is not a valid list.")
        print(f"Original List: {sample_list}")
        sample_list.append(99)                        
        print(f"Modified List: {sample_list}")
    except Exception as error:
        print(f"An unexpected runtime error occurred: {error}")