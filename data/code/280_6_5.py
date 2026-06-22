def repeat_action():
    target_number = 5
    for i in range(3):
        print(f"Current number: {i}")
        if i == target_number:
            break

if __name__ == '__main__':
    repeat_action()