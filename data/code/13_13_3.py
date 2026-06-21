from functools import reduce

def snake_to_camel(s):
    words = s.split('_')
    return words[0] + ''.join(w.capitalize() for w in words[1:])

if __name__ == '__main__':
    print(snake_to_camel('get_http_status_code'))