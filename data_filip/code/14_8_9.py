def are_characters_distinct(text: str) -> bool:
    return len(set(text)) == len(text)

if __name__ == '__main__':
    sample = "abcdefg"
    result = are_characters_distinct(sample)
    print(result)