numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))

if __name__ == '__main__':
    print(filtered_numbers)