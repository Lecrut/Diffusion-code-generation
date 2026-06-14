import sys
def main():
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        num1 = int(line1.strip())
        line2 = sys.stdin.readline()
        if not line2:
            return
        num2 = int(line2.strip())
        print(num1 + num2)
    except ValueError:
        sys.stderr.write("Error: Invalid input. Please provide two integers.\n")
    except Exception as e:
        sys.stderr.write(f"An unexpected error occurred: {e}\n")
if __name__ == '__main__':
    try:
        if len(sys.argv) > 1 and sys.argv[1] == "sample":
            print("5 10")
        else:
            main()
    except Exception as e:
        sys.stderr.write(f"Execution failed: {e}\n")