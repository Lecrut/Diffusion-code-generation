def repeat_print(n, count):
    if count == 0:
        return
    repeat_print(n, count - 1)
    print(n)
if __name__ == '__main__':
    start_number = 10
    repetitions = 5
    repeat_print(start_number, repetitions)