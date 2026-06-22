def rle_encode_case_insensitive(text):
    if not text:
        return ""
    
    text = text.lower()
    compressed = []
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = text[i]
            count = 1
    
    compressed.append(f"{current_char}{count}")
    return "".join(compressed)

if __name__ == '__main__':
    sample_data = "AaaBBBccccDDD"
    result = rle_encode_case_insensitive(sample_data)
    print(result)