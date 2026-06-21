from itertools import groupby

def run_length_encode(s):
    if not s:
        return []
    result = []
    for char, group in groupby(s):
        count = sum(1 for _ in group)
        result.append((char, count))
    return result

if __name__ == '__main__':
    sample_string = "aaabbcdddd"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)
    sample_string_2 = "1122233"
    encoded_result_2 = run_length_encode(sample_string_2)
    print(encoded_result_2)
    sample_string_3 = ""
    encoded_result_3 = run_length_encode(sample_string_3)
    print(encoded_result_3)