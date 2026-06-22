def snake_to_camel(s):
    return s[0] + ''.join(w.capitalize() for w in s.split('_')[1:])

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))
    print(snake_to_camel('foo_bar_baz'))
    print(snake_to_camel('single'))