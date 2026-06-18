def remove_spaces(s: str) -> str:
    """Returns a copy of string s with all spaces removed."""
    return "".join(c for c in s if not c == " ")

if __name__ == "__main__":
    samples = ["Hello World", "Python 3.10", "No Spaces Here"]
    result_list = [remove_spaces(s) for s in samples]
    print(result_list[0]) # Output: HelloWorld