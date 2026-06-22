def split_and_filter(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    segments = text.split(',')
    result = []
    for segment in segments:
        stripped = segment.strip()
        if stripped:
            result.append(stripped)
    return result

if __name__ == '__main__':
    sample_input = "apple,  banana , , cherry,  ,  date "
    output = split_and_filter(sample_input)
    print(output)