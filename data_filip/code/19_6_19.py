def run_length_encode(text: str) -> str:
    if not text:
        return ''
    lower_text = text.lower()
    if not lower_text:
        return ''
    result = []
    count = 1
    length = len(lower_text)
    for i in range(1, length):
        if lower_text[i] == lower_text[i - 1]:
            count += 1
        else:
            result.append(f'{count}{lower_text[i - 1]}')
            count = 1
    result.append(f'{count}{lower_text[-1]}')
    return ''.join(result)
if __name__ == '__main__':
    sample_text = 'AAbbCCcDDD'
    encoded = run_length_encode(sample_text)
    print(encoded)