def concatenate_segments(parts: list[str], separator: str = ' ') -> str:
    if not isinstance(parts, list) or not all(isinstance(part, str) for part in parts):
        raise ValueError("All elements of the input list must be strings.")
    if not isinstance(separator, str):
        raise ValueError("Separator must be a string.")
    
    result = ""
    for i, part in enumerate(parts):
        if i > 0:
            result += separator
        result += part
    return result

if __name__ == '__main__':
    parts1 = ["hello", "world", "python"]
    result1 = concatenate_segments(parts1, separator="---")
    print(f"Result 1: {result1}")
    
    parts2 = ["a", "b", "c", "d"]
    result2 = concatenate_segments(parts2)
    print(f"Result 2: {result2}")
    
    parts3 = ["one", "two", "three"]
    result3 = concatenate_segments(parts3, separator=" | ")
    print(f"Result 3: {result3}")
    
    parts4 = ["apple", "banana", "cherry"]
    result4 = concatenate_segments(parts4)
    print(f"Result 4: {result4}")
    
    parts5 = ["test"]
    result5 = concatenate_segments(parts5, separator=":")
    print(f"Result 5: {result5}")