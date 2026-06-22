from itertools import groupby

def run_length_encode(s):
    if not s:
        return ""
    result = []
    for char, group in groupby(s):
        count = sum(1 for _ in group)
        result.append(f"{char}{count}")
    return "".join(result)

if __name__ == "__main__":
    sample_string = "aaabbccccd"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)
    empty_string = ""
    print(run_length_encode(empty_string))
    single_char = "z"
    print(run_length_encode(single_char))