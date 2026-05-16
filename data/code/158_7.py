def main():
    file_name = 'input.txt'
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            for line in content.splitlines():
                try:
                    number = int(line.strip())
                    if number % 2 == 0:
                        print(number)
                except ValueError:
                    continue
    except FileNotFoundError:
        pass
if __name__ == '__main__':
    main()