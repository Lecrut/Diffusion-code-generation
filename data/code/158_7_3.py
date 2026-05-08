def main():
    file_name = 'input.txt'
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            numbers = content.split()
            for item in numbers:
                try:
                    number = int(item)
                    if number % 2 == 0:
                        print(number)
                except ValueError:
                    continue
    except FileNotFoundError:
        pass
if __name__ == '__main__':
    with open('input.txt', 'w') as f:
        f.write("1 2 3 4 5 6 7 8 9 10")
    main()