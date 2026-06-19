def concatenate_segments(iterable, separator):
    for segment in iterable:
        yield segment
        yield separator

def generate_concatenated_string(iterable, separator):
    concatenated = ""
    for item in concatenate_segments(iterable, separator):
        concatenated += item
    return concatenated.rstrip(separator)

if __name__ == '__main__':
    sample_strings = ["dog", "cat", "bird"]
    separator_character = "; "
    final_result = generate_concatenated_string(sample_strings, separator_character)
    print(final_result)