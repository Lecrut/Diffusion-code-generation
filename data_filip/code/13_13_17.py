def snake_to_camel(s):
    return ''.join(w.capitalize() if i > 0 else w for i, w in enumerate(s.split('_')))

if __name__ == '__main__':
    result = snake_to_camel('this_is_a_sample_string')
    print(result)