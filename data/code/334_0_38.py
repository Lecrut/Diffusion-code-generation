import sys
def main():
    str1 = "Hello"
    str2 = "World"
    result = str1 + str2
    print(result)
    return 0
if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)