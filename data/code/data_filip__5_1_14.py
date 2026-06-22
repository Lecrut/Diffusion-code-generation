def capitalize_first_chars(strings):
    result = []
    for s in strings:
        if s:
            result.append(s[0].upper() + s[1:])
        else:
            result.append("")
    return result

if __name__ == "__main__":
    sample_data = ["hello", "world", "", "python", "code", ""]
    print(capitalize_first_chars(sample_data))