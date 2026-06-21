def split_and_filter(input_str):
    segments = input_str.replace('-', ' ').replace('_', ' ').split()
    filtered_segments = [segment for segment in segments if segment.isalnum()]
    return filtered_segments

if __name__ == '__main__':
    sample_text = "example-text_123-world"
    result = split_and_filter(sample_text)
    print(result)