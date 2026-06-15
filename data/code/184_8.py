import sys
def search_file(filename, search_term):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if search_term in line:
                    print(line, end='')
    except IOError as e:
        print(f"Error reading file {filename}: {e}", file=sys.stderr)
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <filename> <search_term>", file=sys.stderr)
    else:
        filename = sys.argv[1]
        search_term = sys.argv[2]
        search_file(filename, search_term)