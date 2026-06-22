def find_min_length_element(strings):
    min_len = float('inf')
    min_element = None
    for string in strings:
        if len(string) < min_len:
            min_len = len(string)
            min_element = string
    return min_element

if __name__ == '__main__':
    sample_values = ["short", "longer", "longest", "tiny"]
    print(find_min_length_element(sample_values))