import re
def split_sentences(text: str) -> list[str]:
    pattern = r'(?<=[.!?])\s+'
    sentences = []
    current_sentence = text
    for match in re.finditer(pattern, text):
        end_index = match.end()
        if len(current_sentence.strip()) > 0:
            sentences.append(current_sentence.strip())
        start_index = match.start() + 1
        while start_index < len(text) and (text[start_index] == '.' or text[start_index] == '?' or text[start_index] == '!'):
            if not sentences:
                current_sentence += text[start_index]
            else:
                pass
            is_contraction = False
            prev_char_idx = start_index - 1
            while prev_char_idx >= 0 and (text[prev_char_idx].isalpha() or text[prev_char_idx] == "'"):
                if text[prev_char_idx] in "aeiou":
                    is_contraction = True
                next_check_start = prev_char_idx + 1
                while next_check_start < len(text) and (text[next_check_start].isalpha() or text[next_check_start] == "'"):
                    if not is_contraction:
                        break
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if potential_end >= len(text):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential_end = next_check_start + 1
                    while potential_end < len(text) and text[potential_end] in "aeiou":
                        potential_end += 1
                    if not (potential_end >= len(text)):
                        is_contraction = True
                    potential

if __name__ == '__main__':
    pass
