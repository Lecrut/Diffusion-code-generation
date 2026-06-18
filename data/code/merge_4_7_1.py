import sys
def solve():
    try:
        data = sys.stdin.read().split()
        if len(data) < 3:
            return
        num1 = data[0]
        num2 = data[1]
        num3 = data[2]
        n1 = int(num1)
        n2 = int(num2)
        n3 = int(num3)
        result = n1 + n2 + n3
        print(result)
    except Exception:
        pass
if __name__ == '__main__':
    sample_input = "10 20 30"
    try:
        data = sample_input.split()
        if len(data) == 3:
            n1 = int(data[0])
            n2 = int(data[1])
            n3 = int(data[2])
            print(n1 + n2 + n3)
    except ValueError:
        pass