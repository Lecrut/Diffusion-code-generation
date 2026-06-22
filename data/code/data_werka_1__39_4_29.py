def is_valid_delimiter(delimiters):
    return isinstance(delimiters, list) and all(isinstance(d, str) and len(d) == 1 for d in delimiters)

def segment_phrase(phrase, delimiters):
    if not is_valid_delimiter(delimiters):
        raise ValueError("Delimiters must be a list of single character strings.")
    
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
    sample_phrase = "apple,banana;orange,grape"
    sample_delimiters = [',', ';']
    try:
        result = segment_phrase(sample_phrase, sample_delimiters)
        print(result)
    except ValueError as e:
        print(e)