def snake_to_camel(snake_str):
    if not snake_str:
        return ""
    
    words = snake_str.split("_")
    
    filtered_words = [w for w in words if w]
    
    if not filtered_words:
        return ""
    
    if len(filtered_words) == 1:
        return filtered_words[0]
    
    camel_parts = [filtered_words[0]] + [word.capitalize() for word in filtered_words[1:]]
    
    return "".join(camel_parts)

if __name__ == "__main__":
    sample_values = [
        "hello_world",
        "simple",
        "already_CamelCase",
        "leading__underscores",
        "__double_leading",
        "trailing__",
        "___multiple",
        "_mixed_case_with_numbers_123_",
        "",
        "a_b_c_d_e",
        "alreadyCamelCase_input",
        "with___many___underscores",
        "_start",
        "end_",
        "a__b",
        "UPPER_CASE",
        "mixed_with_numbers_1_2_3"
    ]
    
    for sample in sample_values:
        result = snake_to_camel(sample)
        print(f"snake_to_camel('{sample}') -> '{result}'")