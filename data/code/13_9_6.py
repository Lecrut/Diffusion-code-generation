def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    sample_snake = "hello_world_example"
    result = to_camel_case(sample_snake)
    print(result)
    another_sample = "user_profile_data"
    print(to_camel_case(another_sample))