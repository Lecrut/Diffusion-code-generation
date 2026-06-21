class StringProcessor:
    def find_smallest(self, data):
        if not data:
            raise ValueError("List cannot be empty")
        return min(data)

if __name__ == '__main__':
    processor = StringProcessor()
    sample_list = ["banana", "apple", "cherry"]
    print(processor.find_smallest(sample_list))