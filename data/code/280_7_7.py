def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"

def repeat_action():
    for i in range(15):
        result = check_even_odd(i)
        print(result)

if __name__ == '__main__':
    repeat_action()