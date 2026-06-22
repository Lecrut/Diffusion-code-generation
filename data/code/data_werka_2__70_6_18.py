import re

CHUNK_SIZE = 64
EMPTY_SENTINEL = object()

def extract_edges(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    if len(input_string) == 0:
        return EMPTY_SENTINEL, EMPTY_SENTINEL

    first_word = EMPTY_SENTINEL
    last_word = EMPTY_SENTINEL
    current_first = True
    last_found_word = EMPTY_SENTINEL
    word_buffer = []
    
    words = re.split(r'\s+', input_string.strip())
    
    if not words:
        return EMPTY_SENTINEL, EMPTY_SENTINEL
        
    first_word = words[0]
    last_found_word = words[-1]
    
    return first_word, last_found_word

if __name__ == '__main__':
    large_text = "start_of_sentence middle_element_1 middle_element_2 end_of_sentence"
    f, l = extract_edges(large_text)
    print(f)
    print(l)