import itertools

def run_length_encode(input_string):
    if not input_string:
        return ""

    compressed_parts = []
    for char, group in itertools.groupby(input_string):
        count = len(list(group))
        compressed_parts.append(f"{char}{count}")

    return "".join(compressed_parts)

if __name__ == '__main__':
    test_string = "aabcccccaaa"
    result = run_length_encode(test_string)
    print(result)