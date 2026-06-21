import collections

def find_double_chars(s):
    counts = collections.Counter(s)
    result = [char for char, count in counts.items() if count == 2]
    return sorted(result)

if __name__ == '__main__':
    sample_string = "programming"
    print(find_double_chars(sample_string))