def snake_to_camel(text):
    parts = text.split('_')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

if __name__ == '__main__':
    result = snake_to_camel('hello_world_example')
    print(result)