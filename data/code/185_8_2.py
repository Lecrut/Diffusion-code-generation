def extract_numbers(text):
    return [float(word) for word in text.split() if word.replace('.', '', 1).isdigit()]

if __name__ == '__main__':
    sample_text = "The temperature is 23.5 degrees, and the pressure is 101.3."
    print(extract_numbers(sample_text))