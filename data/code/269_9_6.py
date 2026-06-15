import re
def tokenize_with_punctuation_separation(text):
    tokens = []
    for char in text:
        if char.isalnum():
            tokens.append(char)
        elif not char.isspace() and not char.isspace():
            tokens.append(char)
        else:
            if tokens and tokens[-1] != ' ':
                tokens.append(' ')
            tokens.append(char)
    return tokens
def tokenize_with_punctuation_separation_optimized(text):
    parts = re.findall(r"[\w']+|[^\w\s]+", text)
    result = []
    for part in parts:
        if part and not (part.isspace() or part.isspace()):
            result.append(part)
        elif part:
            pass                                                          
    tokens = []
    current_token = ""
    for char in text:
        if char.isalnum() or char == '_':
            current_token += char
        else:
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)
    if current_token:
        tokens.append(current_token)
    return tokens
def tokenize_with_punctuation_separation_final(text):
    tokens = re.findall(r"[\w']+|[^\w\s]+", text)
    final_tokens = []
    for i in range(len(tokens)):
        token = tokens[i]
        if not token:
            continue
        if token.isalnum() or token.isalpha():
            final_tokens.append(token)
        else:
            if final_tokens and (final_tokens[-1].isalnum() or final_tokens[-1] == '_'):
                final_tokens.append(token)
            elif not final_tokens:
                final_tokens.append(token)
            else:
                final_tokens.append(token)
    chunks = text.split()
    final_tokens = []
    for chunk in chunks:
        if not chunk:
            continue
        word_parts = re.findall(r"[\w']+|[^\w\s]+", chunk)
        final_tokens.extend(word_parts)
    return final_tokens
if __name__ == '__main__':
    sample_string1 = "Hello, world! How are you?"
    sample_string2 = "This is a test; it works."
    sample_string3 = "Word1.Word2-Word3"
    sample_string4 = "  Test with multiple , and . marks. "
    print(f"Input: '{sample_string1}'")
    result1 = tokenize_with_punctuation_separation_final(sample_string1)
    print(f"Result: {result1}\n")
    print(f"Input: '{sample_string2}'")
    result2 = tokenize_with_punctuation_separation_final(sample_string2)
    print(f"Result: {result2}\n")
    print(f"Input: '{sample_string3}'")
    result3 = tokenize_with_punctuation_separation_final(sample_string3)
    print(f"Result: {result3}\n")
    print(f"Input: '{sample_string4}'")
    result4 = tokenize_with_punctuation_separation_final(sample_string4)
    print(f"Result: {result4}\n")