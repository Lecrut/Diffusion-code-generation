import json
def validate_input(data: str) -> bool:
    try:
        decoded = data.encode('utf-8').decode()
        return len(decoded.strip()) > 0 and not any(char in '<>' for char in decoded)
    except Exception:
        return False
def reverse_sequence(sequence):
    if isinstance(sequence, str):
        reversed_str = sequence[::-1]
        return json.dumps(reversed_str)
    elif isinstance(sequence, list):
        try:
            data = json.loads(sequence)
            if not validate_input(data):
                raise ValueError("Invalid JSON input")
            return [str(item)[::-1] for item in reversed_sequence]
        except Exception as e:
            print(f"Error processing sequence: {e}")
    else:
        print("Unsupported data type")
if __name__ == '__main__':
    sample_inputs = ["Hello, World!", "[1, 2, 3]", '{"key": "value"}']
    for item in sample_inputs:
        try:
            result = reverse_sequence(item)
            if isinstance(result, str):
                print(f"Input: {item} -> Output: {result}")
            else:
                print(f"Input: {item} -> Output: {json.dumps(result)}")
        except Exception as e:
            print(f"Error with input '{item}': {e}")