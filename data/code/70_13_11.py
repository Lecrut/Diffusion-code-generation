class ListProcessor:
    @staticmethod
    def print_first_last(items):
        if items:
            print(f"{items[0]} {items[-1]}")
        else:
            print("List is empty")

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    ListProcessor.print_first_last(sample_list)