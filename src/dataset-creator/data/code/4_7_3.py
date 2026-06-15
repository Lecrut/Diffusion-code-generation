import sys
def solve():
    data = sys.stdin.read().split()
    if len(data) < 3:
        return
    try:
        a = int(data[0])
        b = int(data[1])
        c = int(data[2])
        result = a + b + c
        print(result)
    except ValueError:
        pass
if __name__ == '__main__':
    sample_input = "10 20 30"
    try:
        data = sample_input.split()
        if len(data) >= 3:
            a = int(data[0])
            b = int(data[1])
            c = int(data[2])
            print(a + b + c)
    except ValueError:
        pass