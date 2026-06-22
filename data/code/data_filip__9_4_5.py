def safe_strip(value):
    if not isinstance(value, str):
        value = str(value)
    return value.strip()

if __name__ == '__main__':
    sample_inputs = ["  hello  ", 42, "  world  ", None, "\t\ttest\t\t", 3.14]
    for item in sample_inputs:
        print(safe_strip(item))