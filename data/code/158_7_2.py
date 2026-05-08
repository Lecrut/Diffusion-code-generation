def process_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number = int(line.strip())
                    if number % 2 == 0:
                        print(number)
                except ValueError:
                    continue
    except FileNotFoundError:
        pass
if __name__ == '__main__':
    sample_content = "1 2 3 4 5 6 7 8 9 10"
    with open('input.txt', 'w') as f:
        f.write(sample_content)
    process_file('input.txt')