CONSTANTS = {
    'A': 5,
    'B': 3
}

def add_constants():
    return CONSTANTS['A'] + CONSTANTS['B']

if __name__ == '__main__':
    result = add_constants()
    print(result)