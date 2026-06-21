def convert_names_to_list(names_str):
    MAX_LINE_LENGTH = 100
    names = [name.strip() for name in names_str.splitlines() if len(name.strip()) <= MAX_LINE_LENGTH and name.strip()]
    return names

if __name__ == '__main__':
    sample_names = """Alice\nBob
Charlie\tDavid"""
    print(convert_names_to_list(sample_names))