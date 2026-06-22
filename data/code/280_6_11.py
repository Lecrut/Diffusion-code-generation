def repeat_action():
    target_number = 5
    for i in range(3):
        if i == target_number:
            break
        print(f"Action {i+1}")

if __name__ == '__main__':
    repeat_action()