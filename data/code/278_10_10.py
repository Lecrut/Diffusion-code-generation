class ItemPrinter:
    @staticmethod
    def print_items(item_list):
        for item in item_list:
            print(item)

if __name__ == '__main__':
    sample_items = [
        "Apple",
        "Banana",
        "Cherry",
        123,
        "Date"
    ]
    ItemPrinter.print_items(sample_items)