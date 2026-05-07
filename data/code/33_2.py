import sys
if __name__ == '__main__':
    input_data = "  This is a sample string with   various spaces. \nIt has   multiple lines. "
    input_stream = sys.stdin
    data = input_stream.read()
    processed_string = "".join(data.split())
    print(processed_string)