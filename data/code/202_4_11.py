def extract_max_value(*args):
    if not args:
        raise ValueError("No arguments provided")
    return max(args)

if __name__ == '__main__':
    print(extract_max_value(10, 5, 20, 8, 15))