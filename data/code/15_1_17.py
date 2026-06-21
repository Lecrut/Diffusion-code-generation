from itertools import groupby

CHAR_COUNT_THRESHOLD = 1
ORIGINAL_LENGTH_MULTIPLIER = 2

def compress_repeated_chars(source_string):
    if not source_string:
        return ""
    parts = []
    for char, group in groupby(source_string):
        count = sum(1 for _ in group)
        if count > CHAR_COUNT_THRESHOLD:
            parts.append(char + str(count))
        else:
            parts.append(char)
    compressed = "".join(parts)
    if len(compressed) * ORIGINAL_LENGTH_MULTIPLIER > len(source_string):
        return source_string
    return compressed

if __name__ == '__main__':
    sample_input = 'aaaaabbbbcccd'
    result = compress_repeated_chars(sample_input)
    print(result)