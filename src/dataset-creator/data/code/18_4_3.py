import json
def reverse_sequence(seq):
    if not isinstance(seq, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    reversed_seq = []
    for item in seq:
        try:
            result_item = reverse_sequence(item)
        except Exception:
            if isinstance(item, (str, bytes)):
                result_item = item[::-1]
            else:
                result_item = str(item)[::-1]
        reversed_seq.append(result_item)
    return tuple(reversed_seq)
if __name__ == '__main__':
    sample_data = [
        42,
        "hello",
        (3.14, ["nested"], {"key": "value"}),
        [],
        None
    ]
    try:
        result = reverse_sequence(sample_data)
        print(result)
        json_str = json.dumps(list(result))
        reversed_json = json.loads(json_str)[::-1] if isinstance(reversed_json, list) else str(reversed_json)[::-1]
    except Exception as e:
        print(f"Error occurred during processing: {e}")