def perform_sequence():
    print('Hello')
    result = (2 + 3) * 4
    return result

if __name__ == '__main__':
    for _ in range(3):
        print(perform_sequence())