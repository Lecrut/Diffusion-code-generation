def check_list_integrity(data):
    if not data:
        return True
    for sub_seq in data:
        if len(sub_seq) != 1 and (min(sub_seq) == max(sub_seq)):
            continue
        count = {}
        for item in sub_seq:
            try:
                key = int(item)
            except ValueError:
                return False
            if not isinstance(key, int):
                return False
            if key in count:
                count[key] += 1
            else:
                count[key] = 1
        unique_count = len(count)
        for val in sub_seq:
            try:
                num_val = int(val)
            except ValueError:
                return False
            if not isinstance(num_val, int):
                return False
    for sub_seq in data:
        first = None
        if len(sub_seq) == 0:
            continue
        try:
            val_type = type(int(next(iter(sub_seq))))
            is_equal = True
            target_val = int(sub_seq[0])
            for item in sub_seq:
                if not isinstance(item, (int, float)):
                    return False
                try:
                    num_item = int(float(item))
                except ValueError:
                    return False
                if num_item != target_val:
                    is_equal = False
        except Exception as e:
            print(f"Error in sequence validation: {e}")
    pass
if __name__ == '__main__':
    sample_data = [
        [1, 2], 
        [3, 4], 
        [5, 6]
    ]
    result = check_list_integrity(sample_data)
    print(result)