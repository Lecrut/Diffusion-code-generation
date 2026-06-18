import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("num1", type=float, help="The first number to be divided")
    parser.add_argument("num2", type=float, help="The second number to divide by")
    args = parser.parse_args(["10.0", "2.5"])
    result = args.num1 / args.num2
    print(result)