def item_generator(sequence):
    for item in sequence:
        yield item
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    print("Printing elements using generator:")
    for num in item_generator(data):
        print(num)