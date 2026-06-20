def case_converter(s):
    lower_str = ""
    upper_str = ""
    title_str = ""
    
    title_words = s.split(' ')
    
    for word in title_words:
        title_word = ""
        first_char_appended = False
        for char in word:
            if ord('a') <= ord(char) <= ord('z'):
                lower_str += char
                upper_str += char.upper()
            elif ord('A') <= ord(char) <= ord('Z'):
                lower_str += char.lower()
                upper_str += char
            else:
                lower_str += char
                upper_str += char
            
            if not first_char_appended:
                if 'a' <= char <= 'z':
                    title_word += char.upper()
                elif 'A' <= char <= 'Z':
                    title_word += char
                else:
                    title_word += char
                first_char_appended = True
            else:
                if 'A' <= char <= 'Z':
                    title_word += char.lower()
                else:
                    title_word += char
        title_str += title_word + " "
    
    title_str = title_str.strip()
    lower_str_result = s.lower()
    upper_str_result = s.upper()
    
    return {
        'lower': lower_str_result,
        'upper': upper_str_result,
        'title': title_str
    }

if __name__ == '__main__':
    sample_text = "Hello World Python"
    result = case_converter(sample_text)
    print(result['lower'])
    print(result['upper'])
    print(result['title'])