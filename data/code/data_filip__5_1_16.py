def capitalize_first_characters(strings):
    return [s.capitalize() if s else s for s in strings]

if __name__ == '__main__':
    sample = ["hello", "world", "", "python", "CODE"]
    print(capitalize_first_characters(sample))