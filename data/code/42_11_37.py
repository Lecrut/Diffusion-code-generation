class StringSegmenter:
    DEFAULT_SEPARATOR = ','

    @staticmethod
    def concatenate_segments(strings, separator=DEFAULT_SEPARATOR):
        if not all(isinstance(s, str) for s in strings):
            raise ValueError("All elements of the input list must be strings.")
        if not isinstance(separator, str):
            raise ValueError("Separator must be a string.")
        
        for string in strings:
            yield string + separator

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    custom_separator = "; "
    segmenter = StringSegmenter()
    result_generator = segmenter.concatenate_segments(sample_strings, custom_separator)
    concatenated_result = ''.join(result_generator).rstrip(custom_separator)
    print(concatenated_result)