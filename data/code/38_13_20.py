def count_repeated_letters(text):
    counts = {}
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in counts:
                counts[char_lower] += 1
            else:
                counts[char_lower] = 1
    result = {}
    for key, value in counts.items():
        if value > 1:
            result[key] = value
    return result

if __name__ == '__main__':
    sample_text = "Programming is fun and Python is powerful"
    output_dict = count_repeated_letters(sample_text)
    print(output_dict)