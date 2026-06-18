import json
def validate_input(data: str) -> bool:
    try:
        parsed = json.loads(data.strip())
        if not isinstance(parsed, (str, list)):
            return False
        return True
    except Exception:
        return False
def reverse_sequence(sequence):
    if isinstance(sequence, str):
        return sequence[::-1]
    elif isinstance(sequence, list):
        return reversed(list(reversed(sequence)))
    else:
        raise ValueError("Unsupported data type")
if __name__ == '__main__':
    sample_inputs = [
        '{"type": "string", "value": "Hello"}',
        '[1, 2, 3]',
        'invalid json {',
        '"<script>alert(1)</script>"'
    ]
    for input_str in sample_inputs:
        if validate_input(input_str):
            try:
                parsed = json.loads(input_str)
                result = reverse_sequence(parsed.get("value", parsed))
                print(f"Input: {input_str} -> Output: {result}")
            except Exception as e:
                print(f"Error processing input: {e}")
        else:
            print(f"Invalid Input: {input_str}")