def clean_name(name):
    return name.strip()

def parse_line(line):
    names = line.split(';')
    cleaned_names = [clean_name(name) for name in names if clean_name(name)]
    return cleaned_names

if __name__ == '__main__':
    sample_line = "Alice; Bob ; Charlie;; David"
    print(parse_line(sample_line))