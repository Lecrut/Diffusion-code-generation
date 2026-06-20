def extract_substrings(text, start_marker, end_marker):
    substrings = []
    start_index = 0
    while True:
        start_pos = text.find(start_marker, start_index)
        if start_pos == -1:
            break
        end_pos = text.find(end_marker, start_pos + len(start_marker))
        if end_pos == -1:
            break
        substrings.append(text[start_pos + len(start_marker):end_pos])
        start_index = end_pos + len(end_marker)
    return substrings

if __name__ == '__main__':
    sample_text = "apple<b>banana</b>cherry<b>date</b>elderberry"
    result = extract_substrings(sample_text, "<b>", "</b>")
    print(result)