import itertools

def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""
    result = []
    for char, group in itertools.groupby(input_string):
        count = len(list(group))
        result.append(f"{count}{char}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAAABBBCCDAA"
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)