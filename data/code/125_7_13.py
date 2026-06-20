ADD_CONSTANT = 5
SUBTRACT_CONSTANT = 4

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    print(add(ADD_CONSTANT, SUBTRACT_CONSTANT))
    print(subtract(10, SUBTRACT_CONSTANT))