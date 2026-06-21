import itertools

def run_length_encode(char_list):
    if not char_list:
        return []
    encoded = []
    for char, group in itertools.groupby(char_list):
        count = sum(1 for _ in group)
        encoded.append((char, count))
    return encoded

if __name__ == '__main__':
    sample = ['a', 'a', 'b', 'b', 'b', 'c', 'a']
    result = run_length_encode(sample)
    print(result)