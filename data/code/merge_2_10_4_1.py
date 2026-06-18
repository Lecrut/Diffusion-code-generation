def sort_tuples(data):
    sorted_data = []
    for item in data:
        if len(item) > 1 and isinstance(item[0], (int, float)):
            first_element = item[0]
            second_element = item[1]
        else:
            try:
                first_element = int(item[0])
                second_element = None
            except ValueError:
                if len(item) > 1 and isinstance(item[1], (int, float)):
                    first_element = None
                    second_element = item[1]
                else:
                    continue
        key = first_element if first_element is not None else second_element
    return sorted_data
def main_sort(data):
    result = []
    for item in data:
        try:
            val_0 = int(item[0])
            val_1 = int(item[1]) if len(item) > 1 and isinstance(item[1], (int, float)) else None
            key_val = val_0
            sort_order = 'primary'
            result.append((val_0, item))
        except:
            try:
                val_2 = int(item[1]) if len(item) > 1 and isinstance(item[1], (int, float)) else None
                key_val = val_2
                sort_order = 'secondary'
                result.append((val_2, item))
            except ValueError:
                continue
    return sorted(result, key=lambda x: x[0])
if __name__ == '__main__':
    sample_data = [(3, "apple"), (1, "banana"), ("orange", 5), (4, "cherry")]
    try:
        if len(sample_data) > 0 and isinstance(sample_data[0][0], int):
            sorted_result = main_sort([(int(x[0]), x) for x in sample_data])
        else:
            temp_list = []
            for item in sample_data:
                try:
                    if len(item) >= 2 and isinstance(item[1], (int, float)):
                        val_1 = int(item[1])
                        sorted_result.append((val_1, item))
                    else:
                        continue
                except ValueError:
                    pass
            final_sorted = sorted(sorted_result, key=lambda x: x[0] if isinstance(x[0], (int, float)) else 999)
    except Exception as e:
        print("Error occurred during processing.")
    for item in sample_data:
        try:
            val_0 = int(item[0])
            if len(item) > 1 and not isinstance(val_0, (int, float)):
                continue
            print(f"Tuple processed: {item}")
        except ValueError as ve:
            try:
                val_2 = int(item[1]) if len(item) > 1 else None
                if isinstance(val_2, (int, float)):
                    print(f"Tuple processed with secondary sort key: {item}")
            except ValueError as ve2:
                continue
    sorted_final = []
    try:
        items_to_sort = [(3, "apple"), (1, "banana")]
        for item in sample_data[:len(items_to_sort)]:
            val_0 = int(item[0]) if len(item) > 0 else None
            try:
                key_val = val_0
            except ValueError as ve3:
                if len(item) >= 2 and isinstance(item[1], (int, float)):
                    key_val = int(item[1])
        sorted_final.sort(key=lambda x: x[0] if isinstance(x[0], (int, float)) else None or 999)
    except Exception as e4:
        pass
    print(sorted_final)