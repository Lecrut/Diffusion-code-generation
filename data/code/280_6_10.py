MAX_REPETITIONS = 3
BREAK_NUMBER = 2

def repeat_action(times):
    for i in range(times):
        if i == BREAK_NUMBER:
            break
        print("Action repeated")

if __name__ == '__main__':
    sample_input = "5"
    try:
        num = int(sample_input)
        repeat_action(num)
    except ValueError:
        print("Invalid input. Please enter an integer.")