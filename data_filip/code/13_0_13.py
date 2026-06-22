def snake_to_camel(s):
    words = s.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

if __name__ == '__main__':
    result = snake_to_camel('hello_world_example')
    print(result)