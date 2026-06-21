def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))
    print(snake_to_camel('make_http_request'))
    print(snake_to_camel('already_camel'))
    print(snake_to_camel('simple'))