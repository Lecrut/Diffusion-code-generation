def execute_sequence(action):
    for _ in range(5):
        action()

if __name__ == '__main__':
    def print_message(message):
        print(f"Executing: {message}")

    actions = [
        "First Action",
        "Second Action",
        "Third Action",
        "Fourth Action",
        "Fifth Action"
    ]

    for message in actions:
        execute_sequence(lambda msg=message: print_message(msg))