def split_and_filter(input_string):
    if not input_string:
        return []
    segments = input_string.split(',')
    return [segment.strip() for segment in segments if segment.strip()]

if __name__ == '__main__':
    sample_data = "apple,  banana, , orange,  , grapefruit, , kiwi, lime"
    result = split_and_filter(sample_data)
    print(result)