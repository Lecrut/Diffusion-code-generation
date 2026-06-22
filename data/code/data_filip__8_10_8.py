def split_by_comma(input_string):
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    raw_parts = input_string.split(',')
    trimmed_parts = [part.strip() for part in raw_parts]
    return trimmed_parts

if __name__ == '__main__':
    sample_values = [
        "apple, banana, cherry",
        " apple ,banana, cherry ",
        "one,,three",
        "single",
        "  , ,  ",
        "a,b,c,d,e",
        ""
    ]
    for value in sample_values:
        result = split_by_comma(value)
        print(result)