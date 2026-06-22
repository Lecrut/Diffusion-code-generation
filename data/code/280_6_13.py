def repeat_action_with_condition():
    for i in range(3):
        if i == 2:
            break
        print(f"Action repeated {i+1} times")

if __name__ == '__main__':
    repeat_action_with_condition()