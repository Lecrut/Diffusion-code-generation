def format_string(s):
    return f"{s}, {s.upper()}, {s.title()}"

if __name__ == '__main__':
    sample_string = "hello world"
    formatted_result = format_string(sample_string)
    print(formatted_result)