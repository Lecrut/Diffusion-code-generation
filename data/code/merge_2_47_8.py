import argparse
import sys
def main():
    parser = argparse.ArgumentParser(description="Multiply two integers.")
    parser.add_argument("num1", type=int)
    parser.add_argument("num2", type=int)
    args = parser.parse_args()
    result = args.num1 * args.num2
    if __name__ == '__main__':
        print(result)