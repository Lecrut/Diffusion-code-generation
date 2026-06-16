def repeat_phrase(number):
    phrase = "Repeat an action many times now"
    for _ in range(number):
        print(phrase)
if __name__ == '__main__':
    sample_input = "5"
    try:
        num = int(sample_input)
        repeat_phrase(num)
    except ValueError:
        print("Invalid input. Please enter an integer.")