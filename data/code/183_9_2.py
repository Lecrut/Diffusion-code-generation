def trim_names(name_string):
    return [name.strip() for name in name_string.split('-')]

if __name__ == '__main__':
    sample_names = "  Alice - Bob   - Charlie  "
    trimmed_names = trim_names(sample_names)
    print(trimmed_names)