import itertools

def run_length_encode(text):
    if not text:
        return []
    result = []
    for key, group in itertools.groupby(text):
        count = sum(1 for _ in group)
        result.append((key, count))
    return result

if __name__ == '__main__':
    sample_input = "aaabbccccdddd"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)
    
    sample_input_empty = ""
    encoded_empty = run_length_encode(sample_input_empty)
    print(encoded_empty)
    
    sample_input_single = "x"
    encoded_single = run_length_encode(sample_input_single)
    print(encoded_single)