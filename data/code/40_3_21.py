def extract_initials(text: str) -> str:
    return ' '.join(word[0] for word in text.split() if word)

if __name__ == '__main__':
    sample_text = "Alibaba Cloud is a leading technology company."
    print(extract_initials(sample_text))