def sum_digits_from_string(text):
    return sum(int(ch) for ch in text if ch.isdigit())

if __name__ == '__main__':
    sample_text = "abc123x4y5z6"
    result = sum_digits_from_string(sample_text)
    print(result)