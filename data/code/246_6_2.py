import sys
def solve():
    try:
        data = sys.stdin.read().split()
        if len(data) < 2:
            return
        a = int(data[0])
        b = int(data[1])
        print(a + b)
    except Exception:
        pass
if __name__ == '__main__':
    a = 15
    b = 27
    print(a + b)