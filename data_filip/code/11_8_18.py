import collections

def find_chars_appearing_twice(s):
    counts = collections.Counter(s)
    result = [char for char, count in counts.items() if count == 2]
    return sorted(result)

if __name__ == '__main__':
    sample_string = "programming"
    output = find_chars_appearing_twice(sample_string)
    print(output)