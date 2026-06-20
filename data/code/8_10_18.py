def split_by_comma(input_string):
    if not isinstance(input_string, str):
        return []
    parts = input_string.split(',')
    trimmed_parts = [part.strip() for part in parts]
    return [part for part in trimmed_parts if part]

if __name__ == '__main__':
    sample1 = "apple, banana,  cherry , ,date"
    sample2 = "  one  , two , , three,  "
    sample3 = ""
    sample4 = "single"
    sample5 = ",,,"

    print(split_by_comma(sample1))
    print(split_by_comma(sample2))
    print(split_by_comma(sample3))
    print(split_by_comma(sample4))
    print(split_by_comma(sample5))