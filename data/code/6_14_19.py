def replace_spaces_with_underscores(text: str) -> str:
    if not text:
        return text
    output_parts = []
    for char in text:
        if char == ' ':
            output_parts.append('_')
        else:
            output_parts.append(char)
    return "".join(output_parts)

if __name__ == '__main__':
    test_cases = [
        "Machine Learning Model Training",
        "Single",
        "A B C D E",
        "   triple   spaces   here   ",
        "Mixed_Spaces_And_Underscores_"
    ]
    for case in test_cases:
        transformed = replace_spaces_with_underscores(case)
        print(transformed)