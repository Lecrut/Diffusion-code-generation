def split_csv_string(text):
    if not text:
        return []
    segments = []
    current_segment = []
    in_quotes = False
    for char in text:
        if char == '"':
            in_quotes = not in_quotes
            current_segment.append(char)
        elif char == ',' and not in_quotes:
            segment_str = ''.join(current_segment).strip()
            if segment_str:
                segments.append(segment_str)
            current_segment = []
        else:
            current_segment.append(char)
    last_segment_str = ''.join(current_segment).strip()
    if last_segment_str:
        segments.append(last_segment_str)
    return segments

if __name__ == '__main__':
    sample_csv = 'hello,  ,world,,test,'
    result = split_csv_string(sample_csv)
    print(result)