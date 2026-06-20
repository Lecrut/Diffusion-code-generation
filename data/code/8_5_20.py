def process_text(text: str) -> list[str]:
    parts = text.split(',')
    result = [part.strip() for part in parts]
    return result

if __name__ == '__main__':
    sample_text = "  apple, banana ,  cherry  "
    processed = process_text(sample_text)
    print(processed)