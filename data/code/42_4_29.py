def concatenate_segments(iterable, separator):
    for segment in iterable:
        if not segment:
            continue
        yield segment
        yield separator
if __name__ == '__main__':
    sample_strings = ['hello', 'world', 'this', 'is', 'a', 'test']
    delimiter = '--'
    concatenated_generator = concatenate_segments(sample_strings, delimiter)
    result = ''
    for part in concatenated_generator:
        if not part.strip():
            break
        result += part
    print(result)