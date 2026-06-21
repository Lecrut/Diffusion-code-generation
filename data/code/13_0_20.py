def snake_to_camel(text):
    parts = text.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    sample_input = "hello_world_test_string"
    result = snake_to_camel(sample_input)
    print(result)