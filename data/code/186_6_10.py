def sorted_generator(items):
    for item in sorted(items):
        yield item

if __name__ == '__main__':
    input_data = ["banana", "apple", "cherry", "date", "elderberry"]
    gen = sorted_generator(input_data)
    print(" ".join(next(gen) for _ in range(len(input_data))))