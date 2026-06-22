def snake_to_camel(text):
    if not text:
        return text
    parts = text.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    result = snake_to_camel('hello_world_example')
    print(result)