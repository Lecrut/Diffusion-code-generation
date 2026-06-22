def repeat_action():
    for i in range(3):
        if i == 2:
            break
        print(f"Action {i + 1}")

if __name__ == '__main__':
    repeat_action()