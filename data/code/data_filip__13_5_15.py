def to_camel_case(s: str) -> str:
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    sample = 'hello_world_example'
    result = to_camel_case(sample)
    print(result)