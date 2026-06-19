def segment_phrase(phrase, delimiters):
    segments = []
    current_segment = ""
    
    for char in phrase:
        if char in delimiters:
            if current_segment:
                segments.append(current_segment)
            current_segment = ""
        else:
            current_segment += char
    
    if current_segment:
        segments.append(current_segment)
    
    return segments

if __name__ == '__main__':
    sample_text = "hello-world|this is a test"
    delimiter_set = ['-', '|', ' ']
    result_segments = segment_phrase(sample_text, delimiter_set)
    print(result_segments)