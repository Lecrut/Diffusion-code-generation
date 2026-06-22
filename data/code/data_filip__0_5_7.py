import unicodedata

def extract_digits(mixed_string):
    result = []
    for char in mixed_string:
        if unicodedata.category(char).startswith('Nd'):
            result.append(int(char))
    return result

if __name__ == '__main__':
    sample_input = "Room 304 and ۲ ½ tickets, plus ٣ more."
    digits = extract_digits(sample_input)
    print(digits)