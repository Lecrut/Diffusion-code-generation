def split_phrase_by_delimiters(phrase, delimiters):
    result = []
    current_segment = ''
    for char in phrase:
        if char in delimiters:
            if current_segment:
                result.append(current_segment)
                current_segment = ''
        else:
            current_segment += char
    if current_segment:
        result.append(current_segment)
    return result

if __name__ == '__main__':
    sample_phrase = "Hello,world,this is a test"
    delimiters = ", "
    print(split_phrase_by_delimiters(sample_phrase, delimiters))