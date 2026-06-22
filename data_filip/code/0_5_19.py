import unicodedata

def extract_unicode_digits(text: str) -> list[int]:
    result = []
    for char in text:
        if unicodedata.category(char) == 'Nd':
            result.append(int(char))
    return result

if __name__ == '__main__':
    sample_string = "Room 12, Section ٣, Floor ⁵, Code αβγ"
    extracted_digits = extract_unicode_digits(sample_string)
    print(extracted_digits)
    
    empty_string = "No digits here! @#$"
    empty_result = extract_unicode_digits(empty_string)
    print(empty_result)
    
    mixed_unicode = "123٤٥٦⁷⁸⁹"
    mixed_result = extract_unicode_digits(mixed_unicode)
    print(mixed_result)