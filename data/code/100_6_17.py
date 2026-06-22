def validate_and_sequence(bits):
    if not isinstance(bits, str):
        raise ValueError("Input must be a string")
    if len(bits) < 3:
        raise ValueError("Sequence must have at least two inputs and one result")
    for char in bits:
        if char not in '01':
            raise ValueError("Invalid character in sequence")
    return bits

def compute_and_result(inputs):
    result = '1'
    for bit in inputs:
        if bit == '0':
            result = '0'
            break
    return result

def verify_and_operation(sequence):
    validate_and_sequence(sequence)
    input_bits = sequence[:-1]
    actual_result = sequence[-1]
    expected_result = compute_and_result(input_bits)
    return actual_result == expected_result

if __name__ == '__main__':
    valid_seq = "1111"
    invalid_seq = "1101"
    print(verify_and_operation(valid_seq))
    print(verify_and_operation(invalid_seq))