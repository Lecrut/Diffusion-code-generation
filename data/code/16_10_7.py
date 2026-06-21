import itertools

def run_length_encode(input_str):
    if not input_str:
        return ""
    result = []
    for char, group in itertools.groupby(input_str):
        count = sum(1 for _ in group)
        result.append(f"{char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbccccddddeee"
    encoded_value = run_length_encode(sample_input)
    print(encoded_value)
    sample_input_two = "1122334455"
    encoded_value_two = run_length_encode(sample_input_two)
    print(encoded_value_two)
    empty_input = ""
    encoded_empty = run_length_encode(empty_input)
    print(encoded_empty)