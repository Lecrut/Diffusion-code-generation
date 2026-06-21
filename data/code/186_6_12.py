def sorted_generator(items):
    return (item for item in sorted(items))

if __name__ == '__main__':
    input_data = ["banana", "apple", "cherry", "date", "elderberry"]
    generator = sorted_generator(input_data)
    print(" ".join(next(generator) for _ in range(len(input_data))))