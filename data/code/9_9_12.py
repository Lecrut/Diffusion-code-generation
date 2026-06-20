def strip_tuple_whitespace(data):
    if not isinstance(data, tuple):
        raise TypeError("Input must be a tuple")
    
    cleaned = tuple(item.strip() for item in data if isinstance(item, str))
    return cleaned

if __name__ == '__main__':
    original_data = ("  hello  ", "world ", " python", "")
    result = strip_tuple_whitespace(original_data)
    print(result)