def main():
    file_name = 'input.txt'
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            numbers = content.split()
            for item in numbers:
                if item.isdigit():
                    number = int(item)
                    if number % 2 == 0:
                        print(number)
    except FileNotFoundError:
        pass
if __name__ == '__main__':
    main()