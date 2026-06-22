def concatenate_segments(parts: list[str], separator: str = ' ') -> str:
    result = []
    for part in parts:
        if result:
            result.append(separator)
        result.append(part)
    return ''.join(result)

if __name__ == '__main__':
    sample_parts1 = ["hello", "world", "python"]
    separator1 = "---"
    concatenated_result1 = concatenate_segments(sample_parts1, separator1)
    print(f"Concatenated Result 1: {concatenated_result1}")

    sample_parts2 = ["apple", "banana", "cherry"]
    separator2 = ", "
    concatenated_result2 = concatenate_segments(sample_parts2, separator2)
    print(f"Concatenated Result 2: {concatenated_result2}")

    sample_parts3 = ["one", "two"]
    separator3 = "|"
    concatenated_result3 = concatenate_segments(sample_parts3, separator3)
    print(f"Concatenated Result 3: {concatenated_result3}")

    sample_parts4 = ["a", "b", "c", "d"]
    separator4 = "-"
    concatenated_result4 = concatenate_segments(sample_parts4, separator4)
    print(f"Concatenated Result 4: {concatenated_result4}")

    sample_parts5 = ["single"]
    separator5 = ","
    concatenated_result5 = concatenate_segments(sample_parts5, separator5)
    print(f"Concatenated Result 5: {concatenated_result5}")