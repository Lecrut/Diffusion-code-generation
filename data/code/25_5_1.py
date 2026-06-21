from itertools import groupby

def run_length_encode(data):
    if not data:
        return []
    encoded = []
    for key, group in groupby(data):
        count = sum(1 for _ in group)
        encoded.append((key, count))
    return encoded

if __name__ == '__main__':
    sample_input = "AAAABBBCCDAA"
    result = run_length_encode(sample_input)
    print(result)
    
    sample_list = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4]
    result_list = run_length_encode(sample_list)
    print(result_list)