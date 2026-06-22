def get_first_name(names):
    return names[0] if names else None

if __name__ == '__main__':
    names = ['Alice', 'Bob', 'Charlie']
    print(get_first_name(names))