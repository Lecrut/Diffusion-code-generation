TRANSLATION_MAP = {" ": "_"}

def apply_translation_map(source_text, mapping):
    result_chars = []
    for char in source_text:
        new_char = mapping.get(char, char)
        result_chars.append(new_char)
    return "".join(result_chars)

if __name__ == '__main__':
    original_sample = "the quick brown fox jumps"
    transformed_output = apply_translation_map(original_sample, TRANSLATION_MAP)
    print(transformed_output)