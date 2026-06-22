def execute_sequence():
    actions = {
        'greeting': 'Hello',
        'addition_result': 2 + 3,
        'multiplication_result': (2 + 3) * 4
    }
    return actions

if __name__ == '__main__':
    for _ in range(3):
        seq = execute_sequence()
        print(seq['greeting'])
        print(seq['multiplication_result'])