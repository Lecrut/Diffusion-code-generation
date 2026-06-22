def repeat_action(limit):
    actions = {
        1: "Action One",
        2: "Action Two",
        3: "Action Three"
    }
    for i in range(1, limit + 1):
        if i in actions:
            print(actions[i])
        else:
            break

if __name__ == '__main__':
    sample_limit = 3
    repeat_action(sample_limit)