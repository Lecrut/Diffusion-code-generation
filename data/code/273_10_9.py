GREETING = 'Hello'
ADDITION = 2 + 3
MULTIPLICATION_FACTOR = 4

def execute_sequence():
    return GREETING, ADDITION * MULTIPLICATION_FACTOR

if __name__ == '__main__':
    for _ in range(3):
        greeting, result = execute_sequence()
        print(greeting)
        print(result)