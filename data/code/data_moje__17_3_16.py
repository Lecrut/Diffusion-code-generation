def get_last_element(collection):
    return collection[-1]

if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]
    print(get_last_element(numbers))
    letters = ('a', 'b', 'c')
    print(get_last_element(letters))