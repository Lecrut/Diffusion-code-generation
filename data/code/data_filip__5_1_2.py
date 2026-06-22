def capitalize_first_char_list(strings):
    result = []
    for s in strings:
        if s == "":
            result.append("")
        else:
            result.append(s[0].upper() + s[1:])
    return result

if __name__ == '__main__':
    sample_data = ["hello", "world", "", "python", "a", "test", ""]
    output = capitalize_first_char_list(sample_data)
    print(output)