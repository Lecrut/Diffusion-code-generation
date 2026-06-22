def repeat_sequence(actions):
    if not isinstance(actions, dict) or len(actions) != 5:
        raise ValueError("actions must be a dictionary with exactly five key-value pairs")
    for i in range(1, 6):
        print(actions.get(i))

if __name__ == '__main__':
    actions = {
        1: "Action One",
        2: "Action Two",
        3: "Action Three",
        4: "Action Four",
        5: "Action Five"
    }
    repeat_sequence(actions)