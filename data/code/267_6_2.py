def process_words(filename):
    try:
        with open(filename, 'r') as file:
            words = file.readlines()
            for line in words:
                word = line.strip()
                if len(word) > 10:
                    print(f"LONG:{word}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError as e:
        print(f"Error reading file: {e}")
if __name__ == '__main__':
    with open('input.txt', 'w') as f:
        f.write("short\n")
        f.write("thisisalongword\n")
        f.write("anotherword\n")
        f.write("verylongwordexample\n")
        f.write("medium\n")
    process_words('input.txt')