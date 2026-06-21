def check_and_operation(sequence: str) -> bool:
    if not sequence:
        return False
    for char in sequence:
        if char not in ('0', '1'):
            raise ValueError("Input must contain only '0' and '1'")
    length = len(sequence)
    if length < 2:
        return False
    inputs = sequence[:-1]
    result = sequence[-1]
    all_inputs_one = True
    for bit in inputs:
        if bit != '1':
            all_inputs_one = False
            break
    expected_result = '1' if all_inputs_one else '0'
    return result == expected_result

if __name__ == '__main__':
    print(check_and_operation("111"))
    print(check_and_operation("101"))
    print(check_and_operation("000"))
    print(check_and_operation("110"))