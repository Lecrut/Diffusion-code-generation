def extract_first_name():
    names = ["Alice", "Bob", "Charlie"]
    if not names:
        return None
    return names[0]

if __name__ == '__main__':
    print(extract_first_name())