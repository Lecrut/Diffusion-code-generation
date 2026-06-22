def split_meaningful_csv(csv_string: str) -> list:
    if not csv_string:
        return []
    segments = csv_string.split(',')
    result = []
    for segment in segments:
        if segment.strip():
            result.append(segment.strip())
    return result

if __name__ == '__main__':
    sample_input = "apple,,banana,, ,orange,,grape"
    output = split_meaningful_csv(sample_input)
    print(output)
    sample_input_empty = ",,,"
    output_empty = split_meaningful_csv(sample_input_empty)
    print(output_empty)
    sample_input_normal = "one,two,three"
    output_normal = split_meaningful_csv(sample_input_normal)
    print(output_normal)