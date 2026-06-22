def repeat_action_with_condition():
    target_number = 5
    current_number = 0

    for _ in range(3):
        if current_number == target_number:
            break
        print(f"Current number: {current_number}")
        current_number += 1

if __name__ == '__main__':
    repeat_action_with_condition()