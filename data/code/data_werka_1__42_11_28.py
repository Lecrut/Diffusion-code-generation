def concatenate_segments(parts: list[str], separator: str = ' ') -> str:
    for i, part in enumerate(parts):
        if i > 0:
            yield separator
        yield part

if __name__ == '__main__':
    parts1 = ["hello", "world", "python"]
    result1 = ''.join(concatenate_segments(parts1, separator="---"))
    print(f"Result 1: {result1}")
    
    parts2 = ["a", "b", "c", "d"]
    result2 = ''.join(concatenate_segments(parts2, separator=" "))
    print(f"Result 2: {result2}")
    
    parts3 = ["one", "two", "three"]
    result3 = ''.join(concatenate_segments(parts3, separator=" | "))
    print(f"Result 3: {result3}")
    
    parts4 = ["start", "end"]
    result4 = ''.join(concatenate_segments(parts4, separator=":"))
    print(f"Result 4: {result4}")
    
    parts5 = ["single"]
    result5 = ''.join(concatenate_segments(parts5, separator=","))
    print(f"Result 5: {result5}")