def item_generator(sequence):
    for item in sequence:
        yield item
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print("Printing items using generator:")
    for number in item_generator(sample_list):
        print(number)