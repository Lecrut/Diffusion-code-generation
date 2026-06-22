def repeat_action(action, times):
    if times <= 0:
        return
    action()
    repeat_action(action, times - 1)

if __name__ == '__main__':
    def print_number():
        print(42)
    
    repeat_action(print_number, 3)