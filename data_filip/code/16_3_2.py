from itertools import groupby

def run_length_encode(char_list):
    result = []
    for key, group in groupby(char_list):
        count = sum(1 for _ in group)
        result.append((key, count))
    return result

if __name__ == '__main__':
    sample_input = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c']
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)