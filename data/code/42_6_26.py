def join_strings_efficiently(string_list):
    return "".join(string_list)

if __name__ == '__main__':
    words = ["efficient", "string", "joining"]
    joined_string = join_strings_efficiently(words)
    print(joined_string)
    
    phrases = ["hello,", "world!", "python."]
    result_phrase = join_strings_efficiently(phrases)
    print(result_phrase)
    
    parts = ["a", "b", "c", "d", "e"]
    combined_parts = join_strings_efficiently(parts)
    print(combined_parts)