def get_third(iterable):
    return (x for x in enumerate(iterable) if x[0] == 2).__next__()

if __name__ == '__main__':
    result = get_third([10, 20, 30, 40])
    print(result)