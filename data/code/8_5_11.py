def split_and_strip(text: str) -> list:
    raw_parts = text.split(',')
    cleaned_parts = []
    for segment in raw_parts:
        cleaned_parts.append(segment.strip())
    return cleaned_parts

if __name__ == '__main__':
    sample_input = "  red , green ,  blue , yellow  , purple"
    output_list = split_and_strip(sample_input)
    print(output_list)