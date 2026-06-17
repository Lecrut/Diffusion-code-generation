def item_generator(sequence):
    for item in sequence:
        yield item
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    generator = item_generator(data)
    print("Printing items using generator:")
    for number in generator:
        print(number)