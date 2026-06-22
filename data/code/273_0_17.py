def repeat_sequence(action):
    for _ in range(5):
        action()

if __name__ == '__main__':
    def custom_action(index):
        print(f"Action {index} repeated")
    
    actions = [custom_action(i) for i in range(1, 6)]
    repeat_sequence(actions[0])