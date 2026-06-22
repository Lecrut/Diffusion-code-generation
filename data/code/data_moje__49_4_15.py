SIZE = 4
SYMBOL = '*'

def generate_square():
    line = SYMBOL * SIZE
    return [line] * SIZE

if __name__ == '__main__':
    result = generate_square()
    print(result)