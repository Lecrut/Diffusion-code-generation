import sys
if __name__ == '__main__':
    try:
        input_data = sys.stdin.read().split()
        if len(input_data) >= 2:
            num1 = float(input_data[0])
            num2 = float(input_data[1])
            print(num2 - num1)
        else:
            pass
    except ValueError:
        pass
    except Exception:
        pass