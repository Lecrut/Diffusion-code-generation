def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    sample_input = "hello_world_example"
    result = snake_to_camel(sample_input)
    print(result)