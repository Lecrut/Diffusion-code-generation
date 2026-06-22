actions = {
    'print_hello': print('Hello'),
    'add_and_multiply': lambda: (2 + 3) * 4
}

def repeat_sequence():
    for _ in range(3):
        actions['print_hello']()
        result = actions['add_and_multiply']()
        print(result)

if __name__ == '__main__':
    repeat_sequence()