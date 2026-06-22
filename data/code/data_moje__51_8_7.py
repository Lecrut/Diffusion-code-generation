def print_pyramid(rows):
    for i in range(1, rows + 1):
        print(str(i) * i)

if __name__ == '__main__':
    result = print_pyramid(5)
    print(result)