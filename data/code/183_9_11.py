def trim_names(name_string):
    return [name.strip() for name in name_string.split('-')]

if __name__ == '__main__':
    sample_input = "  Alex-Bob - Charlie-Dave  "
    trimmed_names = trim_names(sample_input)
    print(trimmed_names)