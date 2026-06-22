def repeat_action():
    for i in range(15):
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")

if __name__ == '__main__':
    repeat_action()