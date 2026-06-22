def run_length_encode(objects):
    if not objects:
        return []
    encoded = []
    current_item = objects[0]
    count = 1
    for item in objects[1:]:
        if item is current_item:
            count += 1
        else:
            encoded.append((count, current_item))
            current_item = item
            count = 1
    encoded.append((count, current_item))
    return encoded

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3]
    object_ref = object()
    object_ref2 = object()
    mixed_data = [object_ref, object_ref, object_ref2, object_ref2, object_ref, object_ref, object_ref]
    result_int = run_length_encode(sample_data)
    result_obj = run_length_encode(mixed_data)
    print(result_int)
    print(result_obj)