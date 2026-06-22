def repeat_action(number):
    phrase = "Action repeated"
    for _ in range(number):
        print(phrase)
        if _ == 2:
            break

if __name__ == '__main__':
    sample_input = "3"
    try:
        num = int(sample_input)
        repeat_action(num)
    except ValueError:
        print("Invalid input. Please enter an integer.")