class ListProcessor:
    @staticmethod
    def print_indexed_elements(data):
        for index in range(len(data)):
            print(f"Index {index}: {data[index]}")

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date']
    ListProcessor.print_indexed_elements(sample_list)