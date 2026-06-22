import re

def snake_to_camel(snake_str):
    if not snake_str:
        return snake_str
    components = re.sub(r'_+', '_', snake_str).split('_')
    if not components:
        return ''
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    sample_values = [
        "hello_world",
        "make_HTTP_request",
        "alreadyCamel",
        "multiple___underscores___here",
        "simple",
        "_leading_underscore",
        "trailing_underscore_",
        "",
        "a_b_c_d_e",
        "get_http_response_code"
    ]
    for s in sample_values:
        print(snake_to_camel(s))