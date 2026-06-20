def swap_case(s):
    return ''.join(c.lower() if c.isupper() else c.upper() for c in s)

def process_string(text):
    return (text, text.lower(), swap_case(text))

if __name__ == '__main__':
    result = process_string("Hello World")
    print(result)