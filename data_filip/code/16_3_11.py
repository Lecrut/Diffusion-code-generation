from itertools import groupby

def run_length_encode(chars):
    result = []
    for char, group in groupby(chars):
        count = sum(1 for _ in group)
        if count == 1:
            result.append(char)
        else:
            result.append(char)
            result.append(str(count))
    return ''.join(result)

if __name__ == '__main__':
    sample_input = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd']
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)