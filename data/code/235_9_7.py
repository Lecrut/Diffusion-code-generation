PATTERNS = {
    'line': '*'
}

def generate_line(width):
    return PATTERNS['line'] * width

if __name__ == '__main__':
    print(generate_line(10))