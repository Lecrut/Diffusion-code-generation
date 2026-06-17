def split_string(s: str, delimiter: str) -> list[str]:
    return [part for part in s.split(delimiter)]
if __name__ == '__main__':
    test_str = "apple#banana#cherry"
    delimiters_to_try = ['#', 'a']
    result1 = split_string(test_str, '#')
    print(f"Split by '#': {result1}")
    result2 = split_string(test_str, '$')
    print(f"Split by '$' (not found): {result2}")