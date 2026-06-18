def find_greatest(*args):
    return max(args) if args else None
if __name__ == '__main__':
    print(find_greatest(3, 10, -5, 7))