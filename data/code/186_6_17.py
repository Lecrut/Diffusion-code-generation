def sorted_generator(items):
    return (item for item in sorted(items))

if __name__ == '__main__':
    input_data = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_items = sorted_generator(input_data)
    print(" ".join(sorted_items))