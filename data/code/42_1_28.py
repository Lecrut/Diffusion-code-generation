def build_string_from_parts(parts):
    result = []
    for part in parts:
        result.append(part)
    return ' '.join(result)

if __name__ == '__main__':
    sample_parts_1 = ["hello", "world", "from", "Qwen"]
    output_1 = build_string_from_parts(sample_parts_1)
    print(output_1)
    
    sample_parts_2 = ["building", "strings", "efficiently"]
    output_2 = build_string_from_parts(sample_parts_2)
    print(output_2)
    
    sample_parts_3 = ["single"]
    output_3 = build_string_from_parts(sample_parts_3)
    print(output_3)