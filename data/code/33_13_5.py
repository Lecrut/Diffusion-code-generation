def remove_spaces(s: str) -> str:
    return s.replace(" ", "") if isinstance(s, str) else ""

if __name__ == '__main__':
    sample_string = "Hello World"
    result = remove_spaces(sample_string)
    print(result)  # Output: HelloWorld

# This solution is efficient because it uses the built-in string replace method which operates in O(n) time complexity, 
# where n is the length of the input string. It performs a single pass through the characters and avoids creating intermediate data structures or function calls for each character.