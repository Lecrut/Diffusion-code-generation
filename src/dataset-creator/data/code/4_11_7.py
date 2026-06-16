def process_choices(choices):
    actions = {1: "Execute action A", 2: "Execute action B", 3: "Execute action C"}
    for choice in choices:
        if choice == 1:
            print(actions[choice])
        elif choice == 2:
            print(actions[choice])
        elif choice == 3:
            print(actions[choice])
        else:
            print("Invalid choice")
if __name__ == '__main__':
    sample_choices = [1, 2, 4, 3]
    process_choices(sample_choices)