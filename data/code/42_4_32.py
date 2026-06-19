def concatenate_segments(iterable, separator):
    for segment in iterable:
        yield segment
        yield separator

if __name__ == '__main__':
    string_list = ["dog", "cat", "bird"]
    separator_string = "; "
    
    result_generator = concatenate_segments(string_list, separator_string)
    final_result = ''.join(result_generator).rstrip(separator_string)
    
    print(final_result)