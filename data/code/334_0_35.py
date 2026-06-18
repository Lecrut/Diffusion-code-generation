import sys
def main():
    string1 = "Hello"
    string2 = "World!"
    result_string = string1 + string2
    print(result_string)
if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)