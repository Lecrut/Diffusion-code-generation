MAX_NUMBER = 5

def append_numbers() -> list:
    numbers = []
    for i in range(1, MAX_NUMBER + 1):
        numbers.append(i)
    return numbers

if __name__ == '__main__':
    result = append_numbers()
    print(result)