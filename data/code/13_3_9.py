def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    samples = [
        "hello_world",
        "this_is_a_test",
        "alreadyCamel",
        "single",
        "multiple___underscores",
        "leading_",
        "_trailing",
        ""
    ]
    for sample in samples:
        print(snake_to_camel(sample))