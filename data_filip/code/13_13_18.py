def snake_to_camel(s: str) -> str:
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    sample_snake = "this_is_a_test_variable"
    sample_snake_2 = "hello_world"
    print(snake_to_camel(sample_snake))
    print(snake_to_camel(sample_snake_2))