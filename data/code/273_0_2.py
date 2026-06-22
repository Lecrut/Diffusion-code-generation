def repeat_actions():
    actions = {
        1: "Action One",
        2: "Action Two",
        3: "Action Three",
        4: "Action Four",
        5: "Action Five"
    }
    for i in range(1, 6):
        print(actions[i])

if __name__ == '__main__':
    repeat_actions()