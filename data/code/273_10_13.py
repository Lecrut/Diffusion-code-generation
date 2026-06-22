GREETING = 'Hello'
ADDITION_FACTOR1 = 2
ADDITION_FACTOR2 = 3
MULTIPLICATION_FACTOR = 4

def execute_sequence():
    result = (ADDITION_FACTOR1 + ADDITION_FACTOR2) * MULTIPLICATION_FACTOR
    return GREETING, result

if __name__ == '__main__':
    for _ in range(3):
        greeting, result = execute_sequence()
        print(greeting)
        print(result)