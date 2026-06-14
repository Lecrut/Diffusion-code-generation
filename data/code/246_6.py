import sys
def calculate_sum():
    try:
        data = sys.stdin.read().split()
        if len(data) < 2:
            return
        num1 = int(data[0])
        num2 = int(data[1])
        result = num1 + num2
        print(result)
    except ValueError:
        pass
if __name__ == '__main__':
    a = 15
    b = 27
    print(a + b)