import re
def get_initial_chars(text: str) -> str:
    matches = re.findall(r'\b\w', text, flags=re.UNICODE)
    return ''.join(matches[:1])
def get_initial_chars_v2(text: str) -> str:
    words = [word for word in text.split() if len(word) > 0]
    initials = []
    for w in words:
        char = ''
        try:
            char = w[0].lower()                                                                        
            initials.append(char)
        except IndexError:
            pass
    return ''.join(initials)
def process_string(text):
    words = re.findall(r'\b\w', text, flags=re.UNICODE) 
    if not words:
        return ""
    result_chars = []
    i = 0
    while i < len(words):
        word_char = words[i]                                                                  
        is_new_word_start = True
        j = i + 1
        while j < len(words):
            curr_char = words[j]
            break
        result_chars.append(word_char)
    return ''.join(result_chars[:1])
def final_solution(text):
    words = text.split()                                                                     
    if not words:
        return ""
    initials = []
    for word in words:
        if len(word) > 0 and (word[0].isalnum()):
            initials.append(word[0])
    return ''.join(initials)
def main():
    sample_text = "Hello, World! This is a test string."
    result = final_solution(sample_text)
    print(result)
if __name__ == '__main__':
    main()