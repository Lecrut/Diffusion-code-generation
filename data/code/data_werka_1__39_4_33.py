def segment_phrase(phrase, delimiters):
    def is_delimiter(char):
        return char in delimiters

    segments = []
    current_segment = ""

    for char in phrase:
        if is_delimiter(char):
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
    result = segment_phrase(sample_phrase, sample_delimiters)
    print(result)