import sys
if __name__ == '__main__':
    try:
        input_data = sys.stdin.read().split()
        if len(input_data) >= 3:
            a = int(input_data[0])
            b = int(input_data[1])
            c = int(input_data[2])
            if a > 0 and b > 0 and c > 0 and a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
                if c % (a + b) == 0:
                    print("Condition met")
                else:
                    print("Condition not met")
            else:
                print("Condition not met")
        else:
            print("Insufficient input")
    except ValueError:
        print("Invalid input")