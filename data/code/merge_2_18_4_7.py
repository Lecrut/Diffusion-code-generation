import json
def reverse_sequence(seq):
    if not isinstance(seq, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    reversed_seq = []
    for item in seq:
        try:
            result = reverse_sequence(item)
            if isinstance(result, str):
                return "Error: Non-iterable element found."
            else:
                reversed_seq.append(result)
        except TypeError as e:
            continue
    return tuple(reversed_seq)
if __name__ == '__main__':
    sample_data = [1, 2, (3, 4), [[5], [6]], "text", None]
    try:
        result = reverse_sequence(sample_data)
        print(result)
        if isinstance(result, tuple):
            json_output = {
                "type": "tuple",
                "value": list(result)
            }
            print(json.dumps(json_output))
    except Exception as e:
        error_message = str(e)
        print(f"Error occurred: {error_message}")