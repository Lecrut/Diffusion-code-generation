import re

def snake_to_camel(text):
    if '_' not in text:
        return text
    parts = text.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

def snake_to_camel_regex(text):
    return re.sub(r'_([a-zA-Z])', lambda m: m.group(1).upper(), text)

if __name__ == '__main__':
    sample_inputs = ['user_name', 'first_name_last_name', 'api_key_id', 'no_underscores', 'multi_word_variable_name']
    for sample in sample_inputs:
        result = snake_to_camel_regex(sample)
        print(f"{sample} -> {result}")