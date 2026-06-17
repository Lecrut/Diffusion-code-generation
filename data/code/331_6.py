import sys
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: script_name <filename>")
    else:
        filename = sys.argv[1]
        try:
            with open(filename, 'r') as f:
                content = f.read()
            lower_content = content.lower()
            with open(filename, 'w') as f:
                f.write(lower_content)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")