DIFFERENT = "The two entered values differ."
SAME = "The two entered values are the same."

def check_values(a, b):
    return DIFFERENT if a != b else SAME

if __name__ == '__main__':
    num1 = 42
    num2 = 7
    print(check_values(num1, num2))