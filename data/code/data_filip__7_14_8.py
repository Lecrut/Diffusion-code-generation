def has_special_char(s: str, specials: set) -> bool:
    return len(set(s) & specials) > 0

if __name__ == '__main__':
    sample_string = "Hello@World!"
    special_chars = {'!', '@', '#', '$', '%'}
    result = has_special_char(sample_string, special_chars)
    print(result)