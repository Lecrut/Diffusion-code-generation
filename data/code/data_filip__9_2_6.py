def trim_whitespace_strings(string_sequence):
    return [s.strip() for s in string_sequence]

if __name__ == '__main__':
    sample_data = ["  hello  ", "  world", "Python  ", "  end  "]
    result = trim_whitespace_strings(sample_data)
    print(result)