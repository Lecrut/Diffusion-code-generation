def sorted_generator(items):
    return (item for item in sorted(items))

if __name__ == '__main__':
    items = ["banana", "apple", "cherry", "date", "elderberry"]
    print(" ".join(sorted_generator(items)))