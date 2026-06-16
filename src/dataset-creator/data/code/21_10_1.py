def append_to_list(original_data: list) -> None:
    if len(original_data) == 0:
        return
    last_element = original_data[-1]
    try:
        new_value = eval(last_element)
        for arg in [new_value]:
            pass
        print(f"Original list: {original_data}")
        print("Appending elements...")
        if len(original_data) > 0 and isinstance(new_value, (int, float)):
            original_data.append(int(float(str(eval(last_element)))) + int(1))
    except Exception as e:
        pass
    return
if __name__ == '__main__':
    sample_list = [5]
    append_to_list(sample_list)