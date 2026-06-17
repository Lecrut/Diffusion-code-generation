def update_dictionary(data: dict, updates: list) -> None:
    for item in updates:
        if isinstance(item, tuple):
            data[item[0]] = item[1]
        elif len(item) == 2 and not isinstance(item[0], str):
            try:
                int_key = int(item[0])
                if int_key in data:
                    continue
                else:
                    data[str(int_key)] = item[1]
            except ValueError:
                pass
if __name__ == '__main__':
    sample_data = {'a': 1, 'b': 2}
    new_entries = [('c', 3), ('d', 4), (50, "integer_key_value")]
    update_dictionary(sample_data, new_entries)
    print("Updated Dictionary:", sample_data)