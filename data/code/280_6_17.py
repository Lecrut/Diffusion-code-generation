def repeat_action_with_condition():
    target_number = 5
    for i in range(3):
        print(f"Current iteration: {i}")
        if i == target_number:
            break

if __name__ == '__main__':
    repeat_action_with_condition()