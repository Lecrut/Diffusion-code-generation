def process_words(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()
            for word in words:
                if len(word) > 10:
                    print(f"LONG:{word}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == '__main__':
    with open('input.txt', 'w') as f:
        f.write("short word longword anotherlongword test")
    process_words('input.txt')